#!/usr/bin/env python
#
# Copyright 2021 Yoshi Yamaguchi
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

import argparse
import datetime
import os

home=os.getenv('HOME')

# TODO(ymotongpoo): change here configurable
target_dirs = [
    os.path.join(home, 'Downloads'),
    os.path.join(home, 'Pictures'),
]

def main() -> None:
    parser = argparse.ArgumentParser(description="Delete unaccessed old files")
    parser.add_argument('--offset', '-n', type=int, default=3, dest='offset',
                        help="offset days until last access date from the execution time")
    args = parser.parse_args()

    now = datetime.datetime.now()
    for target in target_dirs:
        for root, dirs, files in os.walk(target):
            for f in files:
                delete_old_file(now, args.offset, os.path.join(root, f))

def delete_old_file(now: datetime.datetime, offset: int, f: str) -> None:
    s = os.stat(f)
    atime = datetime.datetime.fromtimestamp(s.st_atime)
    if now - atime > datetime.timedelta(days=offset):
        os.remove(f)

if __name__ == '__main__':
    main()
