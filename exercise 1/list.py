{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOIwBg3iBGu3NSWn0T/2fXc",
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
        "<a href=\"https://colab.research.google.com/github/yves-romeo/soil-test-result/blob/main/list.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "mN43CkL8fJ2R"
      },
      "outputs": [],
      "source": [
        "soil_samples = [55, 78, 42, 85, 63]\n",
        "print(f\"\\nOriginal list of samples: {soil_samples}\")\n",
        "\n",
        "soil_samples.sort()\n",
        "print(f\"Sorted original list: {soil_samples}\")\n",
        "\n",
        "new_sample = 91\n",
        "soil_samples.append(new_sample)\n",
        "print(f\"List after adding a new sample ({new_sample}): {soil_samples}\")\n",
        "\n",
        "if len(soil_samples) > 0 and min(soil_samples) < 50:\n",
        "    soil_samples.remove(min(soil_samples))\n",
        "    print(f\"List after removing a value below 50: {soil_samples}\")\n",
        "\n",
        "soil_samples.sort()\n",
        "print(f\"Final sorted list: {soil_samples}\")"
      ]
    }
  ]
}