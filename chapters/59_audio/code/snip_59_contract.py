from __future__ import annotations

import json

CHAPTER = 59
TITLE = 'Audio, parlato e musica'


def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    waveform = [0.0, 0.5, -0.5, 0.0]
    frame_size = 2
    frames = [waveform[i:i + frame_size] for i in range(0, len(waveform), frame_size)]
    return {"frames": frames, "sample_count": len(waveform), "invariant": "audio framing preserves sample order and declared frame size"}


def main() -> None:
    print(json.dumps(contract(), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
