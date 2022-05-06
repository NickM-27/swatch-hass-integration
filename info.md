<!-- markdownlint-disable first-line-heading -->
<!-- markdownlint-disable no-inline-html -->

<img src="https://raw.githubusercontent.com/NickM-27/swatch-hass-integration/master/images/swatch.png"
     alt="Swatch icon"
     width="16%"
     align="right"
     style="float: right; margin: 10px 0px 20px 20px;" />

[![GitHub Release](https://img.shields.io/github/release/NickM-27/swatch-hass-integration.svg?style=flat-square)](https://github.com/NickM-27/swatch-hass-integration/releases)
[![Build Status](https://img.shields.io/github/workflow/status/NickM-27/swatch-hass-integration/Build?style=flat-square)](https://github.com/NickM-27/swatch-hass-integration/actions/workflows/build.yaml)
[![Test Coverage](https://img.shields.io/codecov/c/gh/NickM-27/swatch-hass-integration?style=flat-square)](https://app.codecov.io/gh/NickM-27/swatch-hass-integration/)
[![License](https://img.shields.io/github/license/NickM-27/swatch-hass-integration.svg?style=flat-square)](LICENSE)
[![hacs](https://img.shields.io/badge/HACS-default-orange.svg?style=flat-square)](https://hacs.xyz)

## Why?

There is great object and face detection software out there, but sometimes AI detection is overkill or not suitable different types of objects. Swatch was created to create an easy to use API to detect the presence of objects of known color in expected places.

In this example you can see a cropped section of the street with a trash can. Then, using expected color bounds, the parts of the image that don't match the expected color are masked away. If a significant enough amount of pixels are left that match the color then it can be considered a true positive.

![crop](https://user-images.githubusercontent.com/14866235/160126079-14dd083c-7ca8-4077-882c-3f5eddeaf6a0.jpg)
![crop-mask](https://user-images.githubusercontent.com/14866235/160126093-82cedb91-c04e-44a2-8f0f-154e084f2f8f.jpg)

[Swatch Custom Component](https://github.com/NickM-27/swatch-hass-integration) for Home Assistant

This is a custom component to integrate [Swatch](https://github.com/NickM-27/swatch) into [Home Assistant](https://www.home-assistant.io).

Provides the following:
- Binary Sensor entities (Zone + Object Sensors)
- Support for multiple Swatch instances.

## Information on Swatch (Available as an Addon)
Efficient and Quick detection of objects based on matching of color.
Easily detect the presence of expected objects in specific locations of camera snapshot
to efficiently react to their presence.

Ex: Look for the green trash can out at the street to know if the trash has been taken out.
