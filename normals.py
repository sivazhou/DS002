{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Copy of template_DS002_normals.ipynb",
      "provenance": [],
      "collapsed_sections": [],
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
        "<a href=\"https://colab.research.google.com/github/sivazhou/DS002/blob/main/normals.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# DS002 Lab: Determine if four datasets have a normal distribution.\n",
        "\n",
        "How do you determine if a data set is normally distributed?\n",
        "In order to be considered a normal distribution, a data set (when graphed) must follow a bell-shaped symmetrical curve centered around the mean. \n",
        "\n",
        "1. Calculate the mean, standard deviation, and the interquartile_range for each dataset. Do they have a normal distribution?\n",
        "\n",
        "2. Plot each dataset as a line plot or as a histogram to see if the data is normally distributed. Include lines showing the median, the mean, and the standard deviation.\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "x0xtXjAMQDOh"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Normality tests\n",
        "\n",
        "> In statistics, normality tests are used to determine if a data set is well-modeled by a [normal distribution](https://en.wikipedia.org/wiki/Normal_distribution) and to compute how likely it is for a [random variable](https://en.wikipedia.org/wiki/Random_variable) underlying the data set to be normally distributed.\n",
        "\n",
        "> More precisely, the tests are a form of model selection, and can be interpreted several ways, depending on one's interpretations of probability:\n",
        "\n",
        "> In [descriptive statistics](https://en.wikipedia.org/wiki/Descriptive_statistics) terms, one measures a goodness of fit of a normal model to the data – if the fit is poor then the data are not well modeled in that respect by a normal distribution, without making a judgment on any underlying variable.\n",
        "\n",
        "> In [frequentist statistics](https://en.wikipedia.org/wiki/Frequentist_statistics) statistical hypothesis testing, data are tested against the null hypothesis that it is normally distributed.\n",
        "\n",
        "## notes\n",
        "+ The goodness of fit of a statistical model describes how well it fits a set of observations.\n",
        "+ A *descriptive statistic* is a summary statistic that quantitatively describes or summarizes features from a collection of information.\n",
        "+ The *null hypothesis* is that two possibilities are the same.\n",
        "+ *Frequentist inference* is a statistical inference which treats “probability” in equivalent terms to “frequency.”"
      ],
      "metadata": {
        "id": "kIbXdIOeP8m9"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Not normal? Try the Central Limit Theorem\n",
        "\n",
        "2. Sample batches of data from each distribution and take the mean of each batch. Then the distribution of the means is going to resemble a Gaussian distribution.\n",
        "\n",
        "> If you sample batches of data from any distribution and take the mean of each batch. Then the distribution of the means is going to resemble a Gaussian distribution. (Same goes for taking the sum) [Read more](https://towardsdatascience.com/the-central-limit-theorem-and-its-implications-4a7adac9d6de)\n"
      ],
      "metadata": {
        "id": "JRDUiW4ltdNv"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Import some data with unusual distributions\n",
        "\n",
        "## Gamma\n",
        "The curve you use to set luminance values on your monitor to better match human perception. \n",
        "\n",
        "https://gist.github.com/douglasgoodwin/714518131330ee1e60dd1b5e0882e80f\n",
        "\n",
        "\n",
        "## LaPlace\n",
        "The Laplace distribution is a continuous probability distribution named after Pierre-Simon Laplace.\n",
        "\n",
        "https://gist.github.com/douglasgoodwin/714518131330ee1e60dd1b5e0882e80f\n",
        "\n",
        "## A photograph\n",
        "This grayscale image has a dark mood. What kimd of distribution does it have?\n",
        "\n",
        "## The first digits of Pi (optional)\n",
        "\n",
        "I have read that the distribution Pi's digital sequence is random, so let's see. The distribution is compoarable to coin flips.\n",
        "\n"
      ],
      "metadata": {
        "id": "2jp8g2rhvevW"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Setup\n",
        "\n",
        "1. import Pyplot\n",
        "2. clone code repo"
      ],
      "metadata": {
        "id": "ZVYpZwxUPvVK"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "PkWLsPyIPcm2"
      },
      "outputs": [],
      "source": [
        "from collections import Counter\n",
        "import seaborn as sns\n",
        "\n",
        "# Plotting cell\n",
        "from matplotlib import pyplot as plt\n",
        "\n",
        "# font\n",
        "plt.rcParams.update({'font.size': 8})\n",
        "\n",
        "# reset the default figsize value\n",
        "plt.rcParams[\"figure.figsize\"] = plt.rcParamsDefault[\"figure.figsize\"]\n",
        "\n",
        "# 144 is good for a high-resolution display. Try 100 if it's too big\n",
        "plt.rcParams[\"figure.dpi\"] = (120)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Import your code from GitHub\n",
        "\n",
        "# This is the root on Google Colab\n",
        "# Use the magic %cd command to navigate around the file system\n",
        "%cd /content/\n",
        "\n",
        "# Use `isdir()` to see if the repository is already here\n",
        "from genericpath import isdir\n",
        "\n",
        "# get your code\n",
        "# Does the folder/directory exist?\n",
        "\n",
        "# Clone the repository with the latest code\n",
        "print(\"Clone the repo\")\n",
        "!git clone https://github.com/sivazhou/DS002.git sivazhou\n",
        "\n",
        "%cd /content/sivazhou\n",
        "!git pull\n",
        "\n",
        "%cd /content/"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1bsRQYkUP0TL",
        "outputId": "02864973-f7a6-465e-cee1-663b1fdf4538"
      },
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content\n",
            "Clone the repo\n",
            "fatal: destination path 'sivazhou' already exists and is not an empty directory.\n",
            "/content/sivazhou\n",
            "remote: Enumerating objects: 7, done.\u001b[K\n",
            "remote: Counting objects: 100% (7/7), done.\u001b[K\n",
            "remote: Compressing objects: 100% (6/6), done.\u001b[K\n",
            "remote: Total 6 (delta 2), reused 0 (delta 0), pack-reused 0\u001b[K\n",
            "Unpacking objects: 100% (6/6), done.\n",
            "From https://github.com/sivazhou/DS002\n",
            "   cab373d..d6e16f8  main       -> origin/main\n",
            "Updating cab373d..d6e16f8\n",
            "Fast-forward\n",
            " anselAdams_blackSun.csv                  | 597 \u001b[32m+++++++++++++++++++++++++++++++\u001b[m\n",
            " anselAdams_blackSun_400x299_inverted.gif | Bin \u001b[31m0\u001b[m -> \u001b[32m102124\u001b[m bytes\n",
            " 2 files changed, 597 insertions(+)\n",
            " create mode 100644 anselAdams_blackSun.csv\n",
            " create mode 100644 anselAdams_blackSun_400x299_inverted.gif\n",
            "/content\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sivazhou import statistics as stats"
      ],
      "metadata": {
        "id": "iHYCShSTX_Xo"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def printInfo(dv):\n",
        "  print(f\"Length: {len(dv)}\")\n",
        "  print(f\"Minimum: {min(dv)}\")\n",
        "  print(f\"Maximum: {max(dv)}\")\n",
        "  print(f\"Mean: {stats.mean(dv)}\")\n",
        "  print(f\"16%,50%,84% Percentile values: {stats.quantile(dv,0.16)},{stats.quantile(dv,0.50)},{stats.quantile(dv,0.84)}\")\n",
        "  print(f\"Median: {stats.median(dv)}\")\n",
        "  print(f\"Std Deviation: {stats.standard_deviation(dv)}\")\n",
        "  print(f\"Interquartile Range: {stats.interquartile_range(dv)}\")"
      ],
      "metadata": {
        "id": "N2QPlIw8zWgZ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Four asymmetrical datasets\n",
        "\n",
        "![skewness and distribution](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Relationship_between_mean_and_median_under_different_skewness.png/868px-Relationship_between_mean_and_median_under_different_skewness.png)\n",
        "\n",
        "# Gamma distribution\n",
        "\n",
        "![gamma curve](https://docs.scipy.org/doc/scipy/_images/scipy-stats-gamma-1.png)"
      ],
      "metadata": {
        "id": "srC714AEq_gh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import csv\n",
        "gamma = []\n",
        "with open('sivazhou/gamma.csv') as csvfile:\n",
        "  rdr = csv.reader(csvfile)\n",
        "  for row in rdr:\n",
        "    gamma.append(float(row[0]))\n",
        "\n",
        "printInfo(gamma)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0FSBeesRUyhn",
        "outputId": "74bf0c33-236b-4cdf-fdb2-ac1adf74fda2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Length: 1000\n",
            "Minimum: 0.07609191985691709\n",
            "Maximum: 9.95054358415928\n",
            "Mean: 1.9321904949508906\n",
            "16%,50%,84% Percentile values: 0.6470909280431079,1.615562777509157,3.1651099383996906\n",
            "Median: None\n",
            "Std Deviation: 1.3840773901336623\n",
            "Interquartile Range: 1.7365660245071104\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.histplot(x=gamma)\n",
        "plt.axvline(x=stats.mean(gamma),color='red')\n",
        "#plt.axvline(x=stats.median(gamma),color='blue')\n",
        "\n",
        "plt.axvline(x=stats.quantile(gamma,0.16),color='black')\n",
        "plt.axvline(x=stats.quantile(gamma,0.84),color='black')\n",
        "#plt.axvline(x=stats.median(gamma),color='blue')\n",
        "\n",
        "plt.title(f\"Gamma distribution with mean (red) and median (blue)\")\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 281
        },
        "id": "E6ZyvKIY12dy",
        "outputId": "34954868-236a-4891-fae0-ec6263af20af"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "def centralLimit(somedata):\n",
        "  # select 100 values using random.sample() function \n",
        "  sample_100 = random.sample(somedata, 100)\n",
        "  # stats.mean(sample_100)\n",
        "\n",
        "  # use for loop to simulate this process 10,000 times\n",
        "  # store each mean into an array called means_size_100\n",
        "  means_size_100 = []\n",
        "  sums_size_100 = []\n",
        "  for _ in range(10000):\n",
        "      sample_size_100 = random.sample(somedata, 100)\n",
        "      means_size_100.append(stats.mean(sample_size_100))\n",
        "      sums_size_100.append(sum(sample_size_100))\n",
        "  return sample_100,means_size_100,sums_size_100\n",
        "\n",
        "sample_100,means_size_100,sums_size_100 = centralLimit(gamma)\n",
        "\n",
        "# plot histogram of 100 samples\n",
        "plt.hist(sample_100)\n",
        "plt.xlabel('Mean')\n",
        "plt.ylabel('Frequency')\n",
        "\n",
        "plt.title('Frequency of Mean');"
      ],
      "metadata": {
        "id": "STlWNAXNHNq9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "outputId": "59f2b73c-9ce5-434b-8fb2-78e1e46c169b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAX4AAAEWCAYAAABhffzLAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAWiElEQVR4nO3de5QlZX3u8e/DAOEaUBkRuY0XxOCFSyao0RgEMSoqGJMoiUpcxjGJGlkxyxBOTtQTPYusg5IYLxGF46iIoogSIYlgMMqKigOiCIioGcJwm1FjuIgS4Hf+qOqTTU/39G6G2tV76vtZq1ZXvVW169d7zTxd+91Vb6WqkCQNx1Z9FyBJmiyDX5IGxuCXpIEx+CVpYAx+SRoYg1+SBsbgl3qWZP8klye5Lckf9V2PtnwGvzqVZG2SO5PcPjI9vO+6lpg3AhdV1c5V9c7ZK5N8IUklOXBW+zlt+2GTKlRbBoNfk/D8qtppZLpxdGWSrfsqbInYF7hygW2+A7x8ZiHJQ4CnABs6rEtbKINfvWjPVF+T5Frg2rbteW2Xx4+T/GuSJ45sf3CSy9rukI8n+ViSt7brfjfJxXO8/qPb+Z9LcnKSf09yS5K/S7J9u+6wJOuSvCHJ+iQ3JXnFyOtsn+TtSa5L8p9JLm7bzkvyulnH/GaSF87z+74gyZXt7/aFJL/Qtv8z8AzgXe2nocfM85adAbw4ybJ2+VjgHOCukWNsleSEJN9L8sMkZyV58Mj6TyS5uf09vpjkcSPrPpjk3e3vdVuSryZ51Dy1aMoZ/OrTMcCTgAOSHAycDrwaeAjwPuDcNrS3BT4NfBh4MPAJ4EWLOM5JwGOAg4BHA3sCfzGy/mHALm37K4F3J3lQu+5k4BeBX26P/UbgXmA18NKZF2i7YfYEzpt98DbMzwSOB5YD5wN/n2Tbqjoc+BLw2vbT0Hfm+R1uBK4CntUuvxz40KxtXkfznv4q8HDgP4B3j6z/B2A/4KHAZTR/TEa9BHgL8CDgu8Db5qlF066qnJw6m4C1wO3Aj9vp0217AYePbPde4C9n7XsNTYg9nSb4MrLuX4G3tvO/C1w8a9+iCfkAdwCPGln3FODf2vnDgDuBrUfWrweeTHNidCdw4By/13Y0wbpfu3wy8J553oP/CZw1srwVcANwWLv8BeD3NvEefgH4PZo/NGcCjwW+065bN/I6VwNHjOy3B/Bfo7/byLpd2/dol3b5g8AHRtY/F/h23/9+nLqZht63qsk4pqounKP9+pH5fYHjZnWfbEtz5lrADdUmUuu6MY+9HNgBuDTJTFuAZSPb/LCq7h5Z/gmwE7AbTcB/b/aLVtVPk3wceGmSt9B0vfzGPDU8fLTeqro3yfU0nxAW41PA24Ef0nz6mW1f4Jwk94603QPsnuRmmjP436R5T2a22Q34z3b+5pH9Zt4DbYHs6lGfRoP8euBtVbXryLRDVZ0J3ATsmZHkBvYZmb+DJtwBSPKwkXU/oDlrf9zI6+5SVeOE2g+AnwLz9XWvBn4HOAL4SVV9eZ7tbqQJ5Zn6AuxNc9Y/tqr6CU13zR8wd/BfDzxn1nu4XVXdAPw2cDTwTJpurRUz5SymBm0ZDH4tFe8Hfj/Jk9LYMclRSXYGvgzcDfxRkm2S/Dpw6Mi+3wAel+SgJNsBb55ZUVX3tq99SpKHAiTZM8mvLVRQu+/pwDuSPDzJsiRPSfJz7fov05w5v525g3jGWcBRSY5Isg3wBuBnNN1Vi3Ui8KtVtXaOdX8HvC3JvgBJlic5ul23c3vMH9L8kfzf9+PY2kIY/FoSqmoN8CrgXTR959+l6bunqu4Cfr1d/hHwYppuj5l9vwP8L+BCmiuE7nOFD/Cn7et9Jcmt7Xb7j1nanwBXAF9rj/1X3Pf/zYeAJwAf2cTvdg1N//zf0nyKeD7NJa53zbfPJl7rxqqa/fvN+BvgXOBzSW4DvkLz5flMndfRfMq4ql2ngcp9u02l6ZDkg8C6qvrznut4ObCqqp7WZx3SYnjGL91PSXYA/hA4te9apMUw+KX7of2OYANwC/DRnsuRFsWuHkkaGM/4JWlgpuIGrt12261WrFjRdxmSNFUuvfTSH1TV8tntUxH8K1asYM2aNX2XIUlTJcmcd7jb1SNJA2PwS9LAGPySNDAGvyQNjMEvSQNj8EvSwBj8kjQwBr8kDYzBL0kDMxV37m6OFSec19ux1550VG/HlqT5eMYvSQNj8EvSwHQW/Em2S3JJkm8kuTLJW9r2RyT5apLvJvl4km27qkGStLEuz/h/BhxeVQcCBwHPTvJkmodVn1JVj6Z5qPYrO6xBkjRLZ8FfjdvbxW3aqYDDgU+27auBY7qqQZK0sU77+JMsS3I5sB64APge8OOqurvdZB2w5zz7rkqyJsmaDRs2dFmmJA1Kp8FfVfdU1UHAXsChwGMXse+pVbWyqlYuX77RA2QkSffTRK7qqaofAxcBTwF2TTJz/8BewA2TqEGS1Ojyqp7lSXZt57cHjgSupvkD8BvtZscBn+mqBknSxrq8c3cPYHWSZTR/YM6qqs8muQr4WJK3Al8HTuuwBknSLJ0Ff1V9Ezh4jvbv0/T3S5J64J27kjQwBr8kDYzBL0kDY/BL0sAY/JI0MAa/JA2MwS9JA2PwS9LAGPySNDAGvyQNjMEvSQNj8EvSwBj8kjQwBr8kDYzBL0kDY/BL0sAY/JI0MAa/JA2MwS9JA2PwS9LAGPySNDAGvyQNjMEvSQNj8EvSwBj8kjQwnQV/kr2TXJTkqiRXJnl92/7mJDckubydnttVDZKkjW3d4WvfDbyhqi5LsjNwaZIL2nWnVNXJHR5bkjSPzoK/qm4Cbmrnb0tyNbBnV8eTJI1nIn38SVYABwNfbZtem+SbSU5P8qB59lmVZE2SNRs2bJhEmZI0CJ0Hf5KdgLOB46vqVuC9wKOAg2g+Ebx9rv2q6tSqWllVK5cvX951mZI0GJ0Gf5JtaEL/jKr6FEBV3VJV91TVvcD7gUO7rEGSdF9dXtUT4DTg6qp6x0j7HiObvRD4Vlc1SJI21uVVPU8FXgZckeTytu1E4NgkBwEFrAVe3WENkqRZuryq52Igc6w6v6tjSpIW5p27kjQwBr8kDYzBL0kDY/BL0sAY/JI0MAa/JA2MwS9JA9PlDVyDt+KE83o57tqTjurluJKmg2f8kjQwBr8kDYzBL0kDY/BL0sAY/JI0MAa/JA2MwS9JA2PwS9LAGPySNDAGvyQNjMEvSQNj8EvSwBj8kjQwBr8kDYzBL0kDY/BL0sB0FvxJ9k5yUZKrklyZ5PVt+4OTXJDk2vbng7qqQZK0sS7P+O8G3lBVBwBPBl6T5ADgBODzVbUf8Pl2WZI0IZ0Ff1XdVFWXtfO3AVcDewJHA6vbzVYDx3RVgyRpYxN55m6SFcDBwFeB3avqpnbVzcDu8+yzClgFsM8++3Rf5BbEZ/1K2pTOv9xNshNwNnB8Vd06uq6qCqi59quqU6tqZVWtXL58eddlStJgjBX8SZ5wf148yTY0oX9GVX2qbb4lyR7t+j2A9ffntSVJ98+4Z/zvSXJJkj9Msss4OyQJcBpwdVW9Y2TVucBx7fxxwGfGrlaStNnGCv6q+hXgd4C9gUuTfDTJkQvs9lTgZcDhSS5vp+cCJwFHJrkWeGa7LEmakLG/3K2qa5P8ObAGeCdwcHtWf+JIN87o9hcDmefljrg/xUqSNt+4ffxPTHIKzSWZhwPPr6pfaOdP6bA+SdIDbNwz/r8FPkBzdn/nTGNV3dh+CpAkTYlxg/8o4M6qugcgyVbAdlX1k6r6cGfVSZIecONe1XMhsP3I8g5tmyRpyowb/NtV1e0zC+38Dt2UJEnq0rjBf0eSQ2YWkvwicOcmtpckLVHj9vEfD3wiyY00l2g+DHhxZ1VJkjozVvBX1deSPBbYv226pqr+q7uyJEldWczonL8ErGj3OSQJVfWhTqqSJHVmrOBP8mHgUcDlwD1tcwEGvyRNmXHP+FcCB7TDKEuSpti4V/V8i+YLXUnSlBv3jH834KoklwA/m2msqhd0UpUkqTPjBv+buyxCkjQ5417O+S9J9gX2q6oLk+wALOu2NElSF8YdlvlVwCeB97VNewKf7qooSVJ3xv1y9zU0T9S6FZqHsgAP7aooSVJ3xg3+n1XVXTMLSbamuY5fkjRlxg3+f0lyIrB9+6zdTwB/311ZkqSujBv8JwAbgCuAVwPnAz55S5Km0LhX9dwLvL+dJElTbNyxev6NOfr0q+qRD3hFkqROLWasnhnbAb8JPPiBL0eS1LWx+vir6ocj0w1V9dc0D2CXJE2Zcbt6DhlZ3IrmE8Am901yOvA8YH1VPb5tezPwKpovigFOrKrzF1mzJGkzjNvV8/aR+buBtcBvLbDPB4F3sfGY/adU1cljHleS9AAb96qeZyz2havqi0lWLHY/SVK3xu3q+eNNra+qdyzimK9N8nJgDfCGqvqPRewrSdpM497AtRL4A5rB2fYEfh84BNi5ncb1XppHOB4E3MR9u5DuI8mqJGuSrNmwYcN8m0mSFmncPv69gEOq6jb4/1/SnldVL13Mwarqlpn5JO8HPruJbU8FTgVYuXKl4wJJ0gNk3DP+3YG7RpbvatsWJckeI4svpHmkoyRpgsY94/8QcEmSc9rlY4DVm9ohyZnAYcBuSdYBbwIOS3IQzV3Aa2nG/ZEkTdC4V/W8Lck/AL/SNr2iqr6+wD7HztF82iLrkyQ9wMbt6gHYAbi1qv4GWJfkER3VJEnq0LiPXnwT8KfAn7VN2wAf6aooSVJ3xj3jfyHwAuAOgKq6kcVdxilJWiLGDf67qqpoh2ZOsmN3JUmSujRu8J+V5H3ArkleBVyID2WRpKm04FU9SQJ8HHgscCuwP/AXVXVBx7VJkjqwYPBXVSU5v6qeABj2kjTlxu3quSzJL3VaiSRpIsa9c/dJwEuTrKW5sic0Hwae2FVhkqRuLPQUrX2q6t+BX5tQPZKkji10xv9pmlE5r0tydlW9aBJFSZK6s1Aff0bmH9llIZKkyVgo+GueeUnSlFqoq+fAJLfSnPlv387Df3+5+/OdVidJesBtMviratmkCpEkTcZihmWWJG0BDH5JGhiDX5IGxuCXpIEx+CVpYAx+SRqYcQdpkxa04oTzejv22pOO6u3Y0rTxjF+SBsbgl6SBMfglaWA6C/4kpydZn+RbI20PTnJBkmvbnw/q6viSpLl1ecb/QeDZs9pOAD5fVfsBn2+XJUkT1FnwV9UXgR/Naj4aWN3OrwaO6er4kqS5TbqPf/equqmdvxnYfb4Nk6xKsibJmg0bNkymOkkagN6+3K2qYhMPd6mqU6tqZVWtXL58+QQrk6Qt26SD/5YkewC0P9dP+PiSNHiTDv5zgePa+eOAz0z4+JI0eF1eznkm8GVg/yTrkrwSOAk4Msm1wDPbZUnSBHU2Vk9VHTvPqiO6OqYkaWHeuStJA2PwS9LAGPySNDAGvyQNjMEvSQNj8EvSwBj8kjQwBr8kDYzBL0kDY/BL0sAY/JI0MAa/JA2MwS9JA2PwS9LAGPySNDAGvyQNjMEvSQNj8EvSwBj8kjQwBr8kDYzBL0kDs3XfBUi6f1accF4vx1170lG9HFcPHM/4JWlgDH5JGpheunqSrAVuA+4B7q6qlX3UIUlD1Gcf/zOq6gc9Hl+SBsmuHkkamL6Cv4DPJbk0yaq5NkiyKsmaJGs2bNgw4fIkacvVV/A/raoOAZ4DvCbJ02dvUFWnVtXKqlq5fPnyyVcoSVuoXoK/qm5of64HzgEO7aMOSRqiiQd/kh2T7DwzDzwL+Nak65Ckoerjqp7dgXOSzBz/o1X1jz3UIUmDNPHgr6rvAwdO+riSpIaXc0rSwDhIm7YIDlgmjc8zfkkaGINfkgbG4JekgTH4JWlgDH5JGhiDX5IGxss5pc3Q12Wk0ubwjF+SBsbgl6SBMfglaWAMfkkaGINfkgbG4JekgTH4JWlgDH5JGhiDX5IGxuCXpIEx+CVpYAx+SRoYB2mTNDWGOCheF8919oxfkgbG4JekgTH4JWlgegn+JM9Ock2S7yY5oY8aJGmoJh78SZYB7waeAxwAHJvkgEnXIUlD1ccZ/6HAd6vq+1V1F/Ax4Oge6pCkQerjcs49getHltcBT5q9UZJVwKp28fYk18zaZDfgB51U2A3r7c401QpTXm/+qsdKxjNN7++CtW7m+73vXI1L9jr+qjoVOHW+9UnWVNXKCZa0Way3O9NUK1hv16ap3r5q7aOr5wZg75Hlvdo2SdIE9BH8XwP2S/KIJNsCLwHO7aEOSRqkiXf1VNXdSV4L/BOwDDi9qq68Hy81bzfQEmW93ZmmWsF6uzZN9fZSa6qqj+NKknrinbuSNDAGvyQNzNQF/7QN95Dk9CTrk3yr71oWkmTvJBcluSrJlUle33dNm5JkuySXJPlGW+9b+q5pIUmWJfl6ks/2XctCkqxNckWSy5Os6buehSTZNcknk3w7ydVJntJ3TfNJsn/7vs5MtyY5fmLHn6Y+/na4h+8AR9Lc+PU14NiquqrXwjYhydOB24EPVdXj+65nU5LsAexRVZcl2Rm4FDhmqb6/SQLsWFW3J9kGuBh4fVV9pefS5pXkj4GVwM9X1fP6rmdTkqwFVlbVVNwMlWQ18KWq+kB7xeAOVfXjvutaSJtrNwBPqqrrJnHMaTvjn7rhHqrqi8CP+q5jHFV1U1Vd1s7fBlxNc6f1klSN29vFbdppyZ7JJNkLOAr4QN+1bGmS7AI8HTgNoKrumobQbx0BfG9SoQ/TF/xzDfewZINpmiVZARwMfLXfSjat7Tq5HFgPXFBVS7nevwbeCNzbdyFjKuBzSS5th1BZyh4BbAD+b9uV9oEkO/Zd1JheApw5yQNOW/BrApLsBJwNHF9Vt/Zdz6ZU1T1VdRDNHeCHJlmS3WlJngesr6pL+65lEZ5WVYfQjKT7mrbbcqnaGjgEeG9VHQzcAUzDd4DbAi8APjHJ405b8DvcQ8favvKzgTOq6lN91zOu9mP9RcCz+65lHk8FXtD2m38MODzJR/otadOq6ob253rgHJqu1qVqHbBu5BPfJ2n+ECx1zwEuq6pbJnnQaQt+h3voUPtl6WnA1VX1jr7rWUiS5Ul2bee3p/nS/9v9VjW3qvqzqtqrqlbQ/Lv956p6ac9lzSvJju0X/LRdJs8CluyVaVV1M3B9kv3bpiOAJXlRwizHMuFuHljCo3PO5QEc7mFikpwJHAbslmQd8KaqOq3fqub1VOBlwBVtvznAiVV1fo81bcoewOr2qoitgLOqaslfJjkldgfOac4F2Br4aFX9Y78lLeh1wBntSeH3gVf0XM8mtX9QjwRePfFjT9PlnJKkzTdtXT2SpM1k8EvSwBj8kjQwBr8kDYzBL0kDY/BLI5LU6I1VSbZOsmEaRtOUxmXwS/d1B/D49oYwaK6z9u5wbVEMfmlj59OMogmz7qxs72g9vX0OwNeTHN22r0jypSSXtdMvt+2HJfnCyDjxZ7R3SEu9MfiljX0MeEmS7YAnct8RSv8HzXALhwLPAP5PewfmeuDIdlCzFwPvHNnnYOB44ADgkTR3SEu9maohG6RJqKpvtsNSH0tz9j/qWTSDrf1Ju7wdsA9wI/CuJAcB9wCPGdnnkqpaB9AOhbGC5qExUi8Mfmlu5wIn04yz9JCR9gAvqqprRjdO8mbgFuBAmk/SPx1Z/bOR+Xvw/516ZlePNLfTgbdU1RWz2v8JeN1MP32Sg9v2XYCbqupemoHulk2sUmmRDH5pDlW1rqreOceqv6R5xOM3k1zZLgO8BzguyTeAx9JcHSQtSY7OKUkD4xm/JA2MwS9JA2PwS9LAGPySNDAGvyQNjMEvSQNj8EvSwPw/OqOwXua8PrcAAAAASUVORK5CYII=\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# plot histogram of 100 samples tested 10K time\n",
        "plt.hist(means_size_100)\n",
        "plt.xlabel('Mean')\n",
        "plt.ylabel('Frequency')\n",
        "plt.title('Frequency of Mean');"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "id": "gxw4tJDbp4aC",
        "outputId": "3e7eec06-a94f-4135-b2fa-215233cba2eb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# plot histogram of 100 samples tested 10K time\n",
        "plt.hist(sums_size_100)\n",
        "plt.xlabel('Sum')\n",
        "plt.ylabel('Frequency')\n",
        "plt.title('Frequency of Sum');"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "id": "lD6I9o7HsjY7",
        "outputId": "69795f2c-5dd5-463d-ae08-9675c2b2ab37"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "printInfo(means_size_100)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "twhGZ5EX7zOI",
        "outputId": "77327ffd-af1c-45fd-cb8b-941d18552ce9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Length: 10000\n",
            "Minimum: 1.467831839132307\n",
            "Maximum: 2.57513849714467\n",
            "Mean: 1.9313595842449223\n",
            "16%,50%,84% Percentile values: 1.803040944704838,1.9268895433304924,2.061423581759311\n",
            "Median: None\n",
            "Std Deviation: 0.13083430669196291\n",
            "Interquartile Range: 0.17508307162603387\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "printInfo(sums_size_100)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ALNoiJmf71R5",
        "outputId": "45474aed-c1ca-4c15-c7e9-cbd1fd0d80b2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Length: 10000\n",
            "Minimum: 146.78318391323072\n",
            "Maximum: 257.51384971446697\n",
            "Mean: 193.13595842449206\n",
            "16%,50%,84% Percentile values: 180.3040944704838,192.68895433304925,206.1423581759311\n",
            "Median: None\n",
            "Std Deviation: 13.083430669196288\n",
            "Interquartile Range: 17.508307162603415\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# open the image as an array\n",
        "from PIL import Image\n",
        "from numpy import asarray\n",
        "# load the image\n",
        "image = Image.open('sivazhou/anselAdams_blackSun_400x299_inverted.gif')\n",
        "# convert image to numpy array\n",
        "data = asarray(image)\n",
        "print(type(data))\n",
        "# summarize shape\n",
        "print(data.shape)\n",
        "\n",
        "flat = data.flatten()\n",
        "\n",
        "\"\"\"data = []\n",
        "with open('sivazhou/anselAdams_blackSun.csv') as csvfile:\n",
        "  rdr = csv.reader(csvfile)\n",
        "  for row in rdr:\n",
        "    data.append(float(row[0]))\"\"\"\n",
        "#np.savetxt('anselAdams_blackSun.csv',data)\n",
        "\n",
        "# create Pillow image\n",
        "image2 = Image.fromarray(data)\n",
        "print(type(image2))\n",
        "\n",
        "# summarize image details\n",
        "print(image2.mode)\n",
        "print(image2.size)\n",
        "image2\n",
        "\n",
        "# save it as a csv\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 401
        },
        "id": "l0tlsjJy8BnV",
        "outputId": "9b5c62f1-4e14-4c5d-b400-356105dbce3b"
      },
      "execution_count": 45,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'numpy.ndarray'>\n",
            "(299, 400)\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "AttributeError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-45-3b1e969713e9>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     20\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     21\u001b[0m \u001b[0;31m# create Pillow image\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 22\u001b[0;31m \u001b[0mimage2\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mImage\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mformarray\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdata\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     23\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtype\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mimage2\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     24\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.7/dist-packages/PIL/Image.py\u001b[0m in \u001b[0;36m__getattr__\u001b[0;34m(name)\u001b[0m\n\u001b[1;32m     59\u001b[0m             \u001b[0m_raise_version_warning\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     60\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0m__version__\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 61\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mAttributeError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"module '{}' has no attribute '{}'\"\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0m__name__\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mname\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     62\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     63\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mAttributeError\u001b[0m: module 'PIL.Image' has no attribute 'formarray'"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "printInfo(flat)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cPFyTz9Iuaa4",
        "outputId": "1909fdd3-5e8d-41f7-9cd3-59a2d3cc3a99"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Length: 119600\n",
            "Minimum: 0\n",
            "Maximum: 231\n",
            "Mean: 44.38982441471572\n",
            "16%,50%,84% Percentile values: 5,23,107\n",
            "Median: 23.0\n",
            "Std Deviation: 54.05626220963892\n",
            "Interquartile Range: 43\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.histplot(x=flat)\n",
        "plt.axvline(x=stats.mean(flat),color='red')\n",
        "plt.axvline(x=stats.quantile(flat,0.16),color='black')\n",
        "plt.axvline(x=stats.quantile(flat,0.84),color='black')\n",
        "plt.axvline(x=stats.median(flat),color='blue')\n",
        "plt.title(f\"Image distribution with mean (red) and median (blue)\")\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 522
        },
        "id": "p7wPP-St8v7Z",
        "outputId": "c0b7bbe8-c739-4d58-e4b2-c4b0c198d898"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 768x576 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "IjYwnFxZ9Isq"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}