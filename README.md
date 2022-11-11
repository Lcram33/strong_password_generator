<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<br />
<div align="center">
  <a href="https://github.com/lcram33/strong_password_generator">
    <img src="images/logo.png" alt="Logo" width="150" height="150">
  </a>

  <h1 align="center">Strong password generator</h1>
  
  <h2 align="center">
    A simple (but complete and fully customizable) program in python to generate cryptographically secure passwords & passphrases.
    <br>
    It generates 6 differents ones, so you can pick the best that fits your needs.
  </h2>

  <h3 align="center">
    <br />
    <a href="https://github.com/lcram33/strong_password_generator/issues">Report Bug</a>
    ·
    <a href="https://github.com/lcram33/strong_password_generator/issues">Request Feature</a>
  </h3>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

![screenshot1]
<br>
![screenshot2]
<br>
![screenshot3]

<p align="left">
  The use is, I think, pretty intuitive. The settings editing is explained in detail.
</p>
<p align="left">
  The standard <b>secrets</b> library is used, to make sure that randomness fits cryptographic usage.
</p>


### Built With

<a href="https://www.python.org">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width=60/>
</a>


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.


### Prerequisites

python3 (should come with your favorite distro)
  ```sh
  sudo apt update && sudo apt install python3
  ```


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/lcram33/strong_password_generator.git
   ```
2. cd into the created folder
   ```sh
   cd strong_password_generator
   ```

3. Start the program
   ```sh
   python3 secure_pwd_gen_console.py
   ```


<!-- USAGE EXAMPLES -->
## Usage

```sh
python3 secure_pwd_gen_console.py
```

That's it ! Just follow the menus and advices given.


### Other programs in this repo

* <i>convert_lists.py</i> is used to convert a text wordlist (one word by line) to a json one (list), for performance (see <i>perf_test.py</i>). The default wordlist is made of English words, but you can switch to french (text file provided).
* <i>extract_quotes.py</i> is a script I made to extract quotes and format them in a file usable in the main program. Feel free to adapt it to add more quotes !


<!-- ROADMAP -->
## Roadmap
<h3>
- 🗹 Base program <br>
- ☐ Graphical interface ? (windowed)
</h3>

See the [open issues](https://github.com/lcram33/strong_password_generator/issues) for a full list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

### Use of code

I chose at some point to split the console part and password/other stuff generator.
Feel free to use the api for your project ! (see examples in the console code)


<!-- CONTACT -->
## Contact

✉️ lcram33@pm.me

Project Link: [https://github.com/lcram33/strong_password_generator](https://github.com/lcram33/strong_password_generator)


## Credits

<a href="https://www.flaticon.com/free-icons/password" title="password icons">Password icons created by Smashicons - Flaticon</a>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/lcram33/strong_password_generator.svg?style=for-the-badge
[contributors-url]: https://github.com/lcram33/strong_password_generator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/lcram33/strong_password_generator.svg?style=for-the-badge
[forks-url]: https://github.com/lcram33/strong_password_generator/network/members
[stars-shield]: https://img.shields.io/github/stars/lcram33/strong_password_generator.svg?style=for-the-badge
[stars-url]: https://github.com/lcram33/strong_password_generator/stargazers
[issues-shield]: https://img.shields.io/github/issues/lcram33/strong_password_generator.svg?style=for-the-badge
[issues-url]: https://github.com/lcram33/strong_password_generator/issues
[license-shield]: https://img.shields.io/github/license/lcram33/strong_password_generator.svg?style=for-the-badge
[license-url]: https://github.com/lcram33/strong_password_generator/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/marc-lecointre
[screenshot1]: images/screenshot1.png
[screenshot2]: images/screenshot2.png
[screenshot3]: images/screenshot3.png
