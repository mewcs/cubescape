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

Timeframe
---------

Approximately four weeks.

Milestones
----------

1. Research

	* Search for available heightmap data.
		- What file formats are used and how well are those formats supported in
		  Python?

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
