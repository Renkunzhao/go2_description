cmake_minimum_required(VERSION 3.10)

project(go2_description)

find_package(ament_cmake REQUIRED)

foreach(dir config dae launch meshes rviz urdf xacro)
	install(DIRECTORY ${dir}/
		DESTINATION share/${PROJECT_NAME}/${dir})
endforeach(dir)

ament_package()
