Changelog
=========

Version 3.0
^^^^^^^^^^^

* Fork renamed to pytemscript. New changes are distributed under GPLv3+
* Complete detailed documentation
* Complete re-write using comtypes library
* Standard scripting interface updated to v1.9
* Added Advanced scripting interface v1.2
* Unified client interface for both local or remote connections
* Initial support for remote execution (socket-based server and client)
* New utility object: Vector
* Validation of returned data types
* Added button events handling
* Development and testing are performed on:

    - Tecnai Spirit (WinXP, Python 3.4)
    - Tecnai F20 (Win7, Python 3.8)
    - Tecnai F30 Polara (WinXP, Python 3.4)
    - Glacios (Win10, Python 3.8)
    - Tundra (Win10, Python 3.11)
    - Titan Krios G1 (Win7, Python 3.6), G2, G3i (Win10, Python 3.8), G4 (Win10, Python 3.8)

Version 2.0.0
^^^^^^^^^^^^^

* C++ adapter removed, COM interface now directly accessed using ``ctypes``
* Raised required minimum Python version to 3.4 (dropped support of Python 2.X)
* More extensive documentation of the high level interfaces and the pytemscript server
* Documentation of known issues of the original scripting interface
* Support of the fluorescent screen
* Separation of STEM detectors and CCD cameras in high level interface
* Deprecation of the methods 'get_detectors', 'get_detector_param', 'set_detector_params', and 'get_optics_state' of 'Microscope' and related classes. See docs for further details.
* Deprecation of the property 'AcqParams' of 'STEMDetector'. See docs for further details.
* Deprecation of the use of 'speed' and 'method' keywords in position dictionary of the 'set_stage_position' method.
* Abstract base class for high level interface
* Test scripts
* More illumination related functions
* TEM/STEM mode control
* Several small improvements and fixes

Version 1.0.10
^^^^^^^^^^^^^^

* Speed keyword added Stage.Goto / Microscope.set_stage_position
* A lot of properties added to Microscope API (DiffShift, ObjStig, CondStig, Projection Mode / SubMode, Magnification, Normalization)
* More properties returned by Microscope.get_optics_state
* Timeout for RemoteMicroscope
* Lots of fixes

Version 1.0.9
^^^^^^^^^^^^^

* Normalization methods in new interface.
* Projective system settings in new interface.

Version 1.0.7
^^^^^^^^^^^^^

Started new interface (with client/server support).

Version 1.0.5
^^^^^^^^^^^^^

* Small fixes
* Clarified license: 3-clause BSD
* Compatibility to Py3K and anaconda distribution

Version 1.0.3
^^^^^^^^^^^^^

* Fixed some small things

Version 1.0.2
^^^^^^^^^^^^^

* Renamed project to temscript.
* Created documentation.

Version 1.0.1
^^^^^^^^^^^^^

* Fixed memory leak related to safearray handling

Version 1.0.0
^^^^^^^^^^^^^

* Initial release
