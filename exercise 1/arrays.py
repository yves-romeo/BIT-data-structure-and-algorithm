{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNI81Px7NfFyiEpXkXvhFIO",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/yves-romeo/soil-test-result/blob/main/arrays.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "uJv02jrvgHqi"
      },
      "outputs": [],
      "source": [
        "import array as arr\n",
        "\n",
        "array_results = arr.array('i', results)\n",
        "\n",
        "array_sum = sum(array_results)\n",
        "\n",
        "print(f\"\\nArray version of results: {array_results}\")\n",
        "print(f\"Sum of the array: {array_sum}\")\n",
        "print(f\"Comparison with list sum: {array_sum == sum(results)}\")"
      ]
    }
  ]
}