# wincam

A fast screen capture library for python on Windows 10 and above (x64 platform only).
This library can capture frames and encode H264 videos using your GPU.

```python
from wincam import DXCamera

with DXCamera(x, y, w, h, fps=30) as camera:
    while True:
        frame, timestamp = camera.get_bgr_frame()
```

See [Demo Video](https://youtu.be/og7-3b0bsuo)

This repo also contains the C++ implementation and a .NET wrapper for
[ScreenRecorder.NET nuget package](src/ScreenRecorder.Net/readme.md).

## Introduction

When you need to capture video frames in a low latency (< 5 milliseconds into a numpy array)
to get a nice smooth 30 or 60 fps video this library can do it.

This is using a new Windows 10 API called
[Direct3D11CaptureFramePool](https://learn.microsoft.com/en-us/uwp/api/windows.graphics.capture.direct3d11captureframepool?view=winrt-26100)
which requires a GPU that supports DirectX 11.

To get the fastest time possible, this library is implemented in C++ on the GPU using DirectX11 and the C++ library
copies each frame directly into a buffer provided by the python code. This C++ library is loaded into your python
process.

## Prerequisites

Requires `Python 3.10` and `Windows 10.0.19041.0` or newer on an `x64` platform.

## Installation

```
pip install wincam
```

See [https://pypi.org/project/wincam/](https://pypi.org/project/wincam/).

## Multiple Monitors

This supports multiple monitors. Windows can define negative X, and Y locations when a monitor is to the left or above
the primary monitor. The `DXCamera` will find and capture the appropriate monitor from the `x, y` locations you provide
and it will crop the image to the bounds you provide.

The `DXCamera` does not support regions that span more than one monitor and it will report an error if you try.

## Examples

The following example scripts are provided in this repo.

- [examples/mirror.py](examples/mirror.py) - shows the captured frames in real time so you can see how it is performing
on your machine. Have some fun with infinite frames with frames!  Press ESCAPE to close the window.

- [examples/video.py](examples/video.py) - records an .mp4 video to disk.

In each example can specify what to record using:
- `--x`, `--y`, `--width`, `--height`, in screen coordinates
- `--hwnd`, a native win32 window handle (which you can find using the inspect tool that comes with the windows SDK)
- `--process`, a win32 process id
- `--point`, an `x,y` screen location from which to find the window that you want to record.


## Performance

Each call to `camera.get_bgr_frame()` can be as fast as 1 millisecond because the C++ code is asynchronously writing to
the buffer provided. This way your python code is not blocking waiting for that frame. For this reason it is crucial
that you use `DXCamera` in a `with` block as shown above since this ensures the life time of the python buffer used by
the C++ code is managed correctly. If you cannot use a `with` block for some reason then you must call the `stop()`
method.

In order to hit a smooth target frame rate while recording video the `DXCamera` takes a target fps as input, which
defaults to 30 frames per second. The calls to `camera.get_bgr_frame()` will self regulate with an accurate sleep
to hit that target as closely as possible so that the frames you collect form a nice smooth video as shown in the
[video.py example](examples/video.py).

Note, there is no point providing an `fps` target greater than the windows monitor refresh rate. You can find this
refresh rate on your Display Settings `Advanced settings` tab. If you go higher than this rate you will only get
duplicate frames since the underlying `Direct3D11CaptureFramePool` is only getting new frames at the refresh rate. This
is normally 60fps, unless you have a fancy new GPU and monitor. On a remote desktop this refresh rate can be lower,
like 30 fps.

Note that this sleep is more accurate that python `time.sleep()` which on Windows is very inaccurate with a
tolerance of +/- 15 milliseconds.  But this more accurate sleep is using a spin wait which uses one core of your CPU.

Note also that windows will only provide a frame if something has changed, so you may request 60fps, but if
things are not updating you may see longer delays between each call to get_bgr_frame.

## Video Encoding

`wincam` also has an optimized way to encode videos directly on your GPU so your python code does not have to poll for
frames and call the opencv VideoWriter.  This results in much smoother videos.

`DXCamera` has an `encode_video` method which takes a filename, and some EncodingProperties including desired frame
rate, and VideoEncodingQuality.  This method encodes the video stream to an H264 encoded .mp4 file.  The method blocks
until another thread calls `stop_encoding`.  You can also specify a maximum seconds to automatically stop encoding after
a certain time.

See the `--native` option on the example `video.py` script for an example.

```pyhton
from wincam import DXCamera, VideoEncodingQuality, EncodingProperties

fps = 60
with DXCamera(x, y, w, h, fps=fps) as camera:
    while True:
        props = EncodingProperties()
        props.frame_rate = fps
        props.quality = VideoEncodingQuality.HD1080p
        props.seconds = 60
        camera.encode_video(filename, props)
```

Will create a 60 second video of the screen bounds at 60fps with HD1080p quality. This can make very smooth
60fps videos at 2560x1440 no problem. You can also get the precise frame capture timings from
`camera.get_frame_times()`.

To create a variable length video based on other input run the encode_video in a background thread then call
`camera.stop_encoding()` to stop it.

# Building the code

To build the C++ code you need Visual Studio 2022 and the Windows SDK version 10.0.26100.0.  You also need to install
the latest FFmpeg binaries, includes and libs from https://ffmpeg.org/download.html then set an environment variable
named  `FFmpegPath` pointing to the installed bin folder where you see `ffmpeg.exe`.

Now load the `src\ScreenCapture.sln` into Visual Studio and select Release, x64 build configuration and select
Build/Rebuild.  Use the `src\build.cmd` command to copy the built binaries to the right location in the
python wincam folder so that `pip install -e .` of your wincam bits will find these newly built binaries.

# Debugging

If you build the debug bits and copy them to the same place build.cmd copies the release bits then you can debug your
python code into the C++ code by setting a breakpoint in VS Code on the native python call like
`self._native.read_next_frame`, then use the interactive view to print the python `os.getpid()` then use your Visual
Studio 2022 instance to "attach debugger" to that python process.  Put a breakpoint on `ReadNextFrame` in
`ScreenCaptureApi.cpp`, not press F10 in the python VS Code instance and it should hit your breakpoint in Visual Studio.

You can also debug using mixed mode .NET debugging in the `WpfTestApp` so you can step directly from .NET into the C++
implementation.

## Credits

This project was inspired by [dxcam](https://github.com/ra1nty/DXcam) and the
[C++ Win32CaptureSample](https://github.com/robmikh/win32capturesample) and was made possible with lots of help from
Windows team members Robert Mikhayelyan and Shawn Hargreaves.

