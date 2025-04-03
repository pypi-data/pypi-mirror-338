# Copyright (c) 2025 Zhendong Peng (pzd17@tsinghua.org.cn)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from io import BytesIO
from typing import List, Optional, Union

import av
from av import error

from .filters import Filter
from .graph import AudioGraph


class StreamReader:
    def __init__(
        self,
        filters: List[Filter] = [],
        format: Optional[str] = None,
        frame_size: Union[int, str] = None,
        return_ndarray: bool = True,
    ):
        self.cache_size = 0
        self.bytestream = BytesIO()
        self.filters = filters
        self.format = format
        self.frame_size = frame_size
        self.graph = None
        self.offset = 0
        self.return_ndarray = return_ndarray

    def push(self, data: bytes):
        self.bytestream.write(data)
        self.cache_size += len(data)

    def pull(self, partial: bool = False):
        # Attempt decoding every `self.cache_size` accumulated bytes.
        if self.cache_size * 2 < self.frame_size and not partial:
            return
        self.cache_size = 0
        try:
            self.bytestream.seek(0)
            container = av.open(self.bytestream, format=self.format)
            stream = container.streams.audio[0]
            # The bytestream is too short to determine the sample rate.
            if stream.sample_rate == 0:
                return
            if self.graph is None:
                self.graph = AudioGraph(stream, self.filters, self.frame_size, self.return_ndarray)

            container.seek(self.offset, any_frame=True, stream=stream)
            # Skip the last frame because it needs to be decoded by the next push.
            frames = list(container.decode(stream))
            for frame in frames[:-1]:
                self.offset = frame.pts + int(frame.samples / stream.sample_rate / stream.time_base)
                self.graph.push(frame)
                yield from self.graph.pull()
            if partial:
                self.graph.push(frames[-1])
            yield from self.graph.pull(partial=partial)
        except (error.EOFError, error.InvalidDataError, error.OSError):
            pass

    def reset(self):
        self.cache_size = 0
        self.bytestream = BytesIO()
        self.graph = None
        self.offset = 0
