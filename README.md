<a id="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Spr1ngLif3/Gemini_BC">
    <img src="utils/media/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Gemini Board Computer</h3>

  <p align="center">
    A simple and affordable board computer for bistage rockets!
    <br />
    <br />
    <a href="https://github.com/Spr1ngLif3/Gemini_BC/software">Scripts</a>
    &middot;
    <a href="https://github.com/Spr1ngLif3/Gemini_BC/hardware/gerbers">Gerbers</a>
    &middot;
    <a href="https://github.com/Spr1ngLif3/Gemini_BC/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#hardware">Hardware</a></li>
        <li><a href="#software">Software</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
<div align="center">
  <img src="./utils/media/board.gif" width="250">
  <img src="./utils/media/launch_video.gif" width="250">
</div>

<br>

Building avionics for rockets can be really difficult: you have to choose the microcontroller, the sensors and how to use it for implement all the feature you want.

The experience looks overwhelming.

This is the right project for you! I developed a first simple platform to implement a complete bistage rocket avionic. This board contains the essential parts for satisfy only two tasks:

1. Starting the second stage of a rocket.
2. Log all the data from the launch in a microSD card.

I used a cheap and modular microcontroller (the Raspberry Pi Pico) for control all the components and I programmed it with the easiest programming language in the world: Python.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Hardware

The board is designed with [KiCAD](https://kicad.org) software, an open source for making schematics and PCBs. 

For editing and take a look to the project, you can open KiCAD and select the option **Open Project (CTRL + O)** in the top-left menu.

After that, **select the .kicd_pro file** in the `hardware` folder.

If you want to send in production the board (with serivces like JLCPCB or PCBWay etc.) you can **zip the `gerbers` folder** and upload the zip file to the production service site. I can also modify the PCB and regenerate the gerbers via KiCAD and make your own board.

#### Note!!!
The KiCAD project needs the TP4056 battery manager footprint to work. You can find it in the `utils` folder. For help KiCAD recognize it, **move the .kicad_mod file in the same folder of the project file**. If you notice some problems, please open a issue or [contact me](#contact).

### Software

1. Install VSCode and setup the environment for the Raspberry Pi Pico. Check this [tutorial](https://randomnerdtutorials.com/raspberry-pi-pico-vs-code-micropython/) (not related to me).
2. Clone the repo.
   ```sh
   git clone https://github.com/Spr1ngLif3/Gemini_BC
   ```
3. Open the `software` folder in VSCode.
   ```sh
   code Gemini_BC/software
   ```
4. Now you can upload the basic script on the board with the command **MicroPico: Upload current file to Pico**. 

**Please do your checks before uploading the scripts and put the board inside a rocket! I'm not responsible for all missusage of this scripts.**


5. Board ready for launch.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

For using it in the wild (in the rocket), be careful to the polarity of the connectors on the board. The battery has a specific polarity but not the igniter (it should not care). I tested the board with some solid rocket engines designed for small rocket models, and I adjusted the timer for the second stage ignition based on the simulation and the specs of the engine.

The board can also charge the battery itself via USB-C with the TP4056 module on board.

Before the launch, be sure that the microSD card is correctly inserted and formatted in the FAT32 filesystem, the battery led is solid blue and the board is well secured on the rocket body.

After that, when you pull the switch to on the Pico boot and start executing the script loaded in it.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue.
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License
Hardware files are licensed under CERN-OHL-S v2.

Software and scripts are licensed under GPLv3.

See `LICENSE` folder for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

IG: [@ilvecchiourlatore](https://instagram.com/ilvecchiourlatore)

Website: [SpaceZero](https://spacezero.it)

<a href="https://www.buymeacoffee.com/spacezero" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-violet.png" alt="Buy Me A Coffee" height="41" width="174"></a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

I list here some resources that I feel useful for you:

* [MicroPython Docs](https://docs.micropython.org/en/latest/)
* [Raspberry Pi Pico Docs](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html)
* [KiCAD Docs](https://docs.kicad.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


Made with <3 by an hacker.


