# 🤖 SelfNav: Autonomous Navigation Workspace

This repository provides a comprehensive ecosystem for developing and simulating autonomous mobile robots using **ROS 2 Humble**. It covers everything from physical robot modeling to SLAM implementation and advanced navigation.

---

## 📂 Project Structure

The workspace is organized into modular packages, each with a specific responsibility:

| Package | Description |
| :--- | :--- |
| `selfbot_bringup` | Main entry point. Contains the launch files that orchestrate the entire system. |
| `selfbot_description` | Defines the physical appearance (URDF/Xacro), 3D meshes, and physical properties for Gazebo simulation. |
| `selfbot_controller` | Manages robot movement, including PID controllers, differential drive, and joystick teleoperation. |
| `selfbot_localization` | Implements localization using **AMCL (Adaptive Monte Carlo Localization)** and Nav2 configuration. |
| `selfbot_mapping` | Configuration for **SLAM Toolbox**, enabling active environment mapping. |
| `selfbot_utils` | Auxiliary tools such as the **Safety Stop** system. |

---

## 🚀 Getting Started

### Prerequisites
- ROS 2 Humble
- Gazebo (Classic or Ignition/Gazebo Sim)
- Nav2 Stack
- SLAM Toolbox

### Main Execution

The `simulated_robot.launch.py` file is the core launcher. It allows you to choose between mapping a new environment or navigating within a known one.

#### 1. Localization Mode (Existing Map) 📍
Use this mode when you already have a saved map and want the robot to navigate within it.
```bash
ros2 launch selfbot_bringup simulated_robot.launch.py use_slam:=false
```
*   **Default Map:** `small_house` (located in `src/selfbot_mapping/maps`).
*   **Technology:** Nav2 AMCL.

#### 2. SLAM Mode (Active Mapping) 🗺️
Use this mode to explore an unknown environment and generate a map in real-time.
```bash
ros2 launch selfbot_bringup simulated_robot.launch.py use_slam:=true
```
*   **Technology:** SLAM Toolbox / Gmapping.

---

## 🛠️ Key Features

*   **Intelligent Safety Stop:** The `safety_stop.py` node monitors laser sensors to prevent imminent collisions, automatically stopping the robot if obstacles are detected too close.
*   **Flexible Control:** Support for manual control via joystick (teleop) or autonomous control through the navigation stack.
*   **Realistic Simulation:** Detailed modeling in Gazebo including friction, inertia, and range sensors (LIDAR).

---

## 📸 Visualization

The system automatically launches **RViz2** with pre-optimized configurations:
- In SLAM mode: Displays the map being built and the laser scan.
- In Localization mode: Displays the loaded map, the AMCL particle cloud, and the global/local path plans.

---

## 🗺️ Map Management

Maps are stored in the following structure within `selfbot_mapping`:
```text
src/selfbot_mapping/maps/
└── small_house/
    ├── map.yaml
    └── map.pgm
```
To use a different map, you can pass the `map_name:=your_map` argument when launching the system.
