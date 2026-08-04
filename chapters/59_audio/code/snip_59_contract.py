from __future__ import annotations

import hashlib
import json
import math
import statistics
from collections import Counter

CHAPTER = 59
TITLE = 'Audio, parlato e musica'


def contract():
    waveform = [0.0, 0.5, -0.5, 0.0]
    frame_size = 2
    frames = [waveform[i:i + frame_size] for i in range(0, len(waveform), frame_size)]
    return {"frames": frames, "sample_count": len(waveform), "invariant": "audio framing preserves sample order and declared frame size"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
