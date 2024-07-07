# WSLBridge
A streamlined utility for path conversion between Windows and WSL, featuring an intuitive GUI for quick Linux command generation.

## Overview
The app offering a straightforward interface with four core functionalities to facilitate file operations between Windows and WSL systems by generating Linux commands:

 - Copy Windows files to Linux.
 - Copy Linux files to Windows.
 - Move Windows files to Linux.
 - Move Linux files to Windows.

Additionally, it provides an efficient method to convert Windows paths to WSL paths, through the `/mnt/`.


**Notice that the app won't run the commands itself, thus you still have to paste the generated commands onto your shell manually.**

## Usage

![image](https://github.com/Ives-Natsume/WSLBridge/assets/134116579/818eaf7b-76cd-4da9-a7c4-2b3ceebff5b0)


- Copy Windows files to Linux

Paste the Windows file path on `Windows File Path`, and the WSL path which you want your file to copy to. Then click the `Copy Windows files to Linux` button below.

Other functions are just similar to the first one, easy to use.


- Win Path to Linux Path

Paste the Windows path you want to operate under WSL environment onto `Windows Target Path`, and click the `Win Path to Linux Path` button below. The program would return the WSL environment path headed of `/mnt/`
