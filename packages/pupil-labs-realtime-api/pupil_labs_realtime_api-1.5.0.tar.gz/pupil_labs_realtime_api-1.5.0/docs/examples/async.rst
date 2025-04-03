Asynchronous Examples
*********************

.. note::
   The examples require Python 3.7+ to run and use the :py:mod:`asyncio` framework.

Remote Control
==============

.. _get_status_example:

Get Current Status
------------------

.. literalinclude:: ../../examples/async/device_status_get_current.py
   :language: python
   :emphasize-lines: 7-8,13-14
   :linenos:

Status Updates
--------------

Wait for status updates from the device

.. literalinclude:: ../../examples/async/device_status_update_wait.py
   :language: python
   :emphasize-lines: 16
   :linenos:

Get a callback when there is a new status updates

.. literalinclude:: ../../examples/async/device_status_update_via_callback.py
   :language: python
   :emphasize-lines: 21,22,25
   :linenos:

Send Event
----------

An event without an explicit timestamp, will be timestamped on arrival at the Neon / Pupil
Invisible Companion device.

.. literalinclude:: ../../examples/async/send_event.py
   :language: python
   :emphasize-lines: 16,20-22
   :linenos:

Start, stop and save, and cancel recordings
-------------------------------------------

.. literalinclude:: ../../examples/async/start_stop_recordings.py
   :language: python
   :emphasize-lines: 23,27
   :linenos:

Templates
-------------------------------------------

You can programmatically fill the template. This allows you to also define the
recording name if the template is created correctly.

.. _async_template_example:

.. literalinclude:: ../../examples/async/templates.py
   :language: python
   :emphasize-lines: 59,61,68-104,110,113
   :linenos:

Streaming
=========

Gaze Data
---------

.. literalinclude:: ../../examples/async/stream_gaze.py
   :language: python
   :emphasize-lines: 16,22-24
   :linenos:

Scene Camera Video
------------------

.. literalinclude:: ../../examples/async/stream_scene_camera_video.py
   :language: python
   :emphasize-lines: 18,24-26
   :linenos:

Eyes Camera Video
------------------

.. literalinclude:: ../../examples/async/stream_eyes_camera_video.py
   :language: python
   :emphasize-lines: 20,28
   :linenos:

.. _stream_video_with_overlayed_gaze_example:

Scene Camera Video With Overlayed Gaze
--------------------------------------

This example processes two streams (video and gaze data) at the same time, matches each
video frame with its temporally closest gaze point, and previews both in a window.

.. literalinclude:: ../../examples/async/stream_video_with_overlayed_gaze.py
   :language: python
   :emphasize-lines: 43,49,70,71
   :linenos:


Device Discovery
================

.. literalinclude:: ../../examples/async/discover_devices.py
   :language: python
   :emphasize-lines: 8,10,15,20
   :linenos:

Time Offset Estimation
======================

See :py:mod:`pupil_labs.realtime_api.time_echo` for details.

.. literalinclude:: ../../examples/async/device_time_offset.py
   :language: python
   :emphasize-lines: 18,27-31,34
   :linenos:
