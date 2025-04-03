from typing import List

from wincam import FpsThrottle, Timer


def test_throttle(test_frames=60, fps=30):
    throttle = FpsThrottle(fps, window_size=1)
    timer = Timer()
    timer.start()
    times: List[float] = []
    previous = None
    for i in range(test_frames):
        timer.sleep(15)
        throttle.step()
        now = timer.ticks()
        if previous is None:
            previous = now
        else:
            times += [now - previous]
            previous = now

    min_step = min(times)
    max_step = max(times)
    avg_step = sum(times) / len(times)

    print(f"frame step times, min: {min_step:.3f}, max: {max_step:.3f}, avg: {avg_step:.3f}")

    with open("times.csv", "w") as f:
        for step in times:
            f.write(f"{step}\n")

    assert len(times) > test_frames * 0.9
    assert len(times) < test_frames * 1.1
    assert avg_step * 1000 > fps * 0.85
    assert avg_step * 1000 < fps * 1.16
