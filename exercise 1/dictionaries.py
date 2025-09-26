{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNkdKZUESmGmfKq57zvW1UF",
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
        "<a href=\"https://colab.research.google.com/github/yves-romeo/soil-test-result/blob/main/dictionaries.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "soil_records = [\n",
        "    {'id': 1, 'name': 'Sample A', 'value': 75},\n",
        "    {'id': 2, 'name': 'Sample B', 'value': 48},\n",
        "    {'id': 3, 'name': 'Sample C', 'value': 92},\n",
        "    {'id': 4, 'name': 'Sample D', 'value': 58}\n",
        "]\n",
        "print(\"\\nOriginal list of dictionaries:\")\n",
        "print(soil_records)\n",
        "\n",
        "for record in soil_records:\n",
        "    if record['name'] == 'Sample B':\n",
        "        record['value'] = 52\n",
        "        break\n",
        "\n",
        "print(\"\\nList after updating 'Sample B':\")\n",
        "print(soil_records)\n",
        "\n",
        "soil_records = [record for record in soil_records if record['id'] != 4]\n",
        "print(\"\\nList after deleting 'Sample D':\")\n",
        "print(soil_records)\n",
        "\n",
        "total_value_from_dict = sum(record['value'] for record in soil_records)\n",
        "print(f\"\\nTotal value from dictionary records: {total_value_from_dict}\")\n",
        "\n"
      ],
      "metadata": {
        "id": "7fVL4qfWg6Jp"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}