cubescape
=========

The purpose of this project is to transform [heightmaps][] into cube landscapes.
The implementation will be done in Python using the [Blender API][].

[heightmaps]: https://en.wikipedia.org/wiki/Heightmap
[Blender API]: http://www.blender.org/documentation/250PythonDoc/

Ideas
-----

* Transform a heightmap into a cubescape.
	- ...

* Colorize the cubes.
	- Use color to differentiate between rivers, forests and mountains.

* Different resolution
	- Use larger cube in areas with lower detail. A large area that is flat could be just one big cube

Timeframe
---------

Approximately four weeks.

Milestones
----------

1. Research
	* Search for available heightmap data.
		- What file formats are used and how well are those formats supported in
		  Python?
			* http://asterweb.jpl.nasa.gov/images/GDEM-10km-BW.png
			* http://visibleearth.nasa.gov/view.php?id=73934
				- Format:
				  "The data are formatted as a single-channel 16-bit integer (two
				  byte, long) signed raw binary file, with big-endian byte order and
				  no header. Dimensions are 86400 columns (width, x) by 43200 lines
				  (height, y)"
	* Get familiar with the Blender API.
		- What subset of the API will be used for this project?


2. Proof of concept.
	* Complete a quick demo which demonstrates the feasibility of the project.
		- Facilitate Blender's scripting capabilities to position a set of cubes.
		- Take performance into consideration! A quick demo should take seconds
		  rather than minutes.

3. Discuss the API and design.
	* How should the project be implemented?
		- Product independent API which returns a list of cube locations. This way
		  the same API could be used in both Blender and Maya.
	* Implement a skeleton structure of the API which includes class, method and
	  function definitions.

4. Implement base functionality.
	* ...
