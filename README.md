# Real Estate Listing Web Service

A web service for real estate listings that combines a Vue.js front end with a CGI-powered search functionality. This project demonstrates how to serve a modern, responsive front end using Vue.js (imported via CDN) and handle real estate search requests via a Python CGI script, all running in Docker containers managed by Docker Compose.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Project](#running-the-project)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project serves as a demo of a **Real Estate Listing Web Service** where:

- **Vue.js** provides a dynamic, responsive user interface.
- A **CGI script** (using Python) handles search queries for real estate listings.
- **Nginx** is configured to serve the static front-end files and route CGI requests through fcgiwrap.
- **Docker Compose** is used to orchestrate the multi-container setup.

## Project Structure

