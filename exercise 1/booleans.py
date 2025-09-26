{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNCYqBVUm8n2fhAOXPFjcns",
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
        "<a href=\"https://colab.research.google.com/github/yves-romeo/soil-test-result/blob/main/booleans.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "XlLkgRhLezsD"
      },
      "outputs": [],
      "source": [
        "threshold = 60\n",
        "\n",
        "if average_value > threshold and min_value > 20:\n",
        "    status_message = \"Status: Above Standard - The soil quality is excellent.\"\n",
        "else:\n",
        "    status_message = \"Status: Below Standard - Further analysis or treatment may be needed.\"\n",
        "\n",
        "print(f\"\\nThreshold Check (Threshold = {threshold}):\")\n",
        "print(status_message)"
      ]
    }
  ]
}