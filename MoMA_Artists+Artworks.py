{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Copy of TEMPLATE_DS002.7.2_MoMA-Artists+Artworks.ipynb",
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
        "<a href=\"https://colab.research.google.com/github/sivazhou/DS002/blob/main/MoMA_Artists%2BArtworks.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# DS002 LAB 7.2\n",
        "## Artworks collected by MoMA\n",
        "\n",
        "The Museum of Modern Art (MoMA) acquired its first artworks in 1929, the year it was established. The collection includes an ever-expanding range of visual expression, including painting, sculpture, printmaking, drawing, photography, architecture, design, film, and media and performance art.\n",
        "\n",
        "As of 2017, the Museum’s collection contained almost 200,000 works from around the world spanning the last 150 years. \n",
        "\n",
        "Content\n",
        "The artists dataset contains 15,091 records, representing all the artists who have work in MoMA's collection and have been cataloged in our database. It includes basic metadata for each artist, including name, nationality, gender, birth year, and death year.\n",
        "\n",
        "The artworks dataset contains 130,262 records, representing all of the works that have been accessioned into MoMA’s collection and cataloged in our database. It includes basic metadata for each work, including title, artist, date, medium, dimensions, and date acquired by the Museum. Some of these records have incomplete information and are noted as “not curator approved.” \n",
        "\n",
        "Your job today is to profile the artists. **You will need to deal with missing and inconsistent data.**\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "-tjaWWAhvLzr"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Please answer these questions:\n",
        "\n",
        "1. How many artists have missing or unusable entries for gender? \n",
        "1. List 100 artists with missing gender. Can you guess why gender was not included?\n",
        "1. What is the ratio of male to female artists? Please make a plot to show.\n",
        "1. How many artists are have missing or unusable entries for Birth Year?\n",
        "1. List the artists with missing Birth Year. How is this related to artists with missing gender?\n",
        "1. What are the top 20 nationalities of the artists? Please plot.\n"
      ],
      "metadata": {
        "id": "2Ogvg9ptOzUy"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 1/ Get the data"
      ],
      "metadata": {
        "id": "IY5LiFPXSC-1"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8MrSa85Du98-",
        "outputId": "6509eeaa-f2a6-4bf9-a1a8-d8f3eeff878f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "rm: cannot remove '*.csv': No such file or directory\n",
            "--2022-03-07 09:42:13--  https://gist.githubusercontent.com/douglasgoodwin/4bebb2445759313a95690de41d338729/raw/5214a3761f648ccc9f3d692eab8a8e9cc8cd3fd7/artists.csv\n",
            "Resolving gist.githubusercontent.com (gist.githubusercontent.com)... 185.199.109.133, 185.199.108.133, 185.199.110.133, ...\n",
            "Connecting to gist.githubusercontent.com (gist.githubusercontent.com)|185.199.109.133|:443... connected.\n",
            "HTTP request sent, awaiting response... 200 OK\n",
            "Length: 610055 (596K) [text/plain]\n",
            "Saving to: ‘artists.csv’\n",
            "\n",
            "artists.csv         100%[===================>] 595.76K  --.-KB/s    in 0.05s   \n",
            "\n",
            "2022-03-07 09:42:14 (11.5 MB/s) - ‘artists.csv’ saved [610055/610055]\n",
            "\n",
            "--2022-03-07 09:42:14--  https://gist.githubusercontent.com/douglasgoodwin/4bebb2445759313a95690de41d338729/raw/5214a3761f648ccc9f3d692eab8a8e9cc8cd3fd7/artworks.csv\n",
            "Resolving gist.githubusercontent.com (gist.githubusercontent.com)... 185.199.109.133, 185.199.108.133, 185.199.110.133, ...\n",
            "Connecting to gist.githubusercontent.com (gist.githubusercontent.com)|185.199.109.133|:443... connected.\n",
            "HTTP request sent, awaiting response... 200 OK\n",
            "Length: 34215052 (33M) [text/plain]\n",
            "Saving to: ‘artworks.csv’\n",
            "\n",
            "artworks.csv        100%[===================>]  32.63M   142MB/s    in 0.2s    \n",
            "\n",
            "2022-03-07 09:42:17 (142 MB/s) - ‘artworks.csv’ saved [34215052/34215052]\n",
            "\n"
          ]
        }
      ],
      "source": [
        "# delete existing copies\n",
        "! rm *.csv ;\n",
        "\n",
        "# Get the data from GitHub\n",
        "!wget https://gist.githubusercontent.com/douglasgoodwin/4bebb2445759313a95690de41d338729/raw/5214a3761f648ccc9f3d692eab8a8e9cc8cd3fd7/artists.csv ;\n",
        "!wget https://gist.githubusercontent.com/douglasgoodwin/4bebb2445759313a95690de41d338729/raw/5214a3761f648ccc9f3d692eab8a8e9cc8cd3fd7/artworks.csv"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Usual imports, Pyplot boilerplate, utility functions\n",
        "\n",
        "1. Set nicer PyPlot defaults\n",
        "1. Include the donutplot function\n",
        "1. Write a function to load CSV data into memory\n",
        "1. Write a function to clean up dates and return a date object\n",
        "1. Write another function to convert the strings you find in the dataset into floating point numbers."
      ],
      "metadata": {
        "id": "x6v3a3yISb7f"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from collections import Counter\n",
        "import random\n",
        "from datetime import datetime, date\n",
        "from dataclasses import dataclass, field\n",
        "from typing import Optional, List, Dict\n",
        "\n",
        "# Plotting cell\n",
        "import seaborn as sns\n",
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
      ],
      "metadata": {
        "id": "VzHu2K3wyAJW"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# code to draw a donut plot\n",
        "# Make a function to display a donut plot\n",
        "\n",
        "def donutplot(keys=[\"yes\",\"no\"],vals=[33,20],legend=\"Are you in a good mood?\"):\n",
        "  # Create a white circle at the center of the plot\n",
        "  my_circle = plt.Circle( (0,0), 0.7, color='white')\n",
        "\n",
        "  # Draw pie wedges with thick white edges\n",
        "  props = {'linewidth':4, 'edgecolor':'white'}\n",
        "  plt.pie(vals,labels=keys,wedgeprops=props )\n",
        "\n",
        "  plt.title(legend)\n",
        "  p = plt.gcf()   # get current figure\n",
        "  p.gca().add_artist(my_circle)\n",
        "\n",
        "  return p"
      ],
      "metadata": {
        "id": "vNfzSV_JzrC5"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Utility functions\n",
        "\n",
        "import csv\n",
        "from pathlib import Path\n",
        "\n",
        "def loadData(source_path: Path) -> List[Dict[str, str]]:\n",
        "  \"\"\"Useful fuction to load local CSV files\"\"\"\n",
        "  with source_path.open() as source_file:\n",
        "    rdr= csv.DictReader(source_file)\n",
        "    data: List[Dict[str, str]] = list(rdr)\n",
        "    return data\n",
        "\n",
        "def string2Date(astring='2000-01-19'):\n",
        "  \"\"\"The dates are a mess, clean them up! Did I miss anything?\"\"\"\n",
        "  try:\n",
        "    if astring == '':\n",
        "      return None\n",
        "    elif 'Unknown' in astring:\n",
        "      return None\n",
        "    elif 'c. ' in astring:\n",
        "      # 'c. 1917'\n",
        "      y = astring.split(' ')[-1]\n",
        "      dto = datetime.strptime(y, '%Y')\n",
        "      return dto\n",
        "    elif astring == 'n.d.':\n",
        "      return None\n",
        "    elif len(astring.split('-')) == 3:\n",
        "      dto = datetime.strptime(astring, '%Y-%m-%d')\n",
        "      return dto\n",
        "    elif len(astring.split('–')) == 2:\n",
        "      # ie date is 1977–78 -- a long hyphen\n",
        "      y = astring.split('–')[0]\n",
        "      dto = datetime.strptime(y, '%Y')\n",
        "      return dto\n",
        "    elif len(astring.split('-')) == 2:\n",
        "      # ie date is 1977-78\n",
        "      y = astring.split('-')[0]\n",
        "      dto = datetime.strptime(y, '%Y')\n",
        "      return dto\n",
        "    else:\n",
        "      dto = datetime.strptime(astring, '%Y')\n",
        "      return dto\n",
        "  except:\n",
        "    return None\n",
        "\n",
        "def string2Float(astring):\n",
        "  if astring == '':\n",
        "    return None\n",
        "  else:\n",
        "    return float(astring)\n",
        "\n",
        "def empty2None(astring):\n",
        "  if astring == '':\n",
        "    return None\n",
        "  else:\n",
        "    return astring.title()"
      ],
      "metadata": {
        "id": "dgzS0X543-VH"
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Use the `dataclass` decorator to make each artist into an object and to help you clean up the data"
      ],
      "metadata": {
        "id": "eL6g7SX8HnZp"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "@dataclass\n",
        "class Artist:\n",
        "    id: int\n",
        "    name: str=None\n",
        "    nationality: str=None\n",
        "    gender: str=None\n",
        "    birth: datetime=None\n",
        "    death: datetime=None\n",
        "\n",
        "    def getMyArtworks(self,artworks):\n",
        "      myartworks = []\n",
        "      for w in artworks:\n",
        "        if self.id in w.artists:\n",
        "          myartworks.append(w)\n",
        "      return myartworks\n",
        "\n",
        "@dataclass\n",
        "class Artwork:\n",
        "    id: int\n",
        "    title: str=\"Untitled\"\n",
        "    # artist: List[Artist]=field(default_factory=list)\n",
        "    artists: List[int]=field(default_factory=list)\n",
        "    name: str=\"unspecified\"\n",
        "    date: datetime=None\n",
        "    medium: str=None\n",
        "    dimensions: str=None\n",
        "    acquired: datetime=None\n",
        "    credit: str=None\n",
        "    catalogue: str=None\n",
        "    department: str=None\n",
        "    classification: str=None\n",
        "    objectnumber: int=None\n",
        "    diameter: int=None\n",
        "    circumference: int=None\n",
        "    height: int=None\n",
        "    length: int=None\n",
        "    width: int=None\n",
        "    depth: int=None\n",
        "    weight: int=None\n",
        "    duration: int=None\n",
        "\n",
        "    def artistDetail(self,artists):\n",
        "      myartists = []\n",
        "      for a in artists:\n",
        "        if a.id in self.artists:\n",
        "          myartists.append(a)\n",
        "      return myartists"
      ],
      "metadata": {
        "id": "tBrq8dQD6661"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Load the CSVs into memory"
      ],
      "metadata": {
        "id": "Bqw66l29YCXf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "artists_csv = loadData(Path(\"/content/artists.csv\"))\n",
        "artists = []\n",
        "\n",
        "for a in artists_csv:\n",
        "  if a['Nationality'] != '':\n",
        "    nation = a['Nationality']\n",
        "  else:\n",
        "    nation = None\n",
        "  artists.append(Artist(int(a['Artist ID']),\n",
        "                        a['Name'],\n",
        "                        nation,\n",
        "                        a['Gender'],\n",
        "                        string2Date(a['Birth Year']),\n",
        "                        string2Date(a['Death Year'])))"
      ],
      "metadata": {
        "id": "DtKHjDSdKVFJ"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "artworks_csv = loadData(Path(\"/content/artworks.csv\"))\n",
        "artworks = []\n",
        "\n",
        "# Artwork ID,Title,Artist ID,Name,Date,Medium,Dimensions,Acquisition Date,Credit,\n",
        "# Catalogue,Department,Classification,Object Number,Diameter (cm),Circumference (cm),Height (cm),\n",
        "# Length (cm),Width (cm),Depth (cm),Weight (kg),Duration (s)\n",
        "\n",
        "for w in artworks_csv:\n",
        "  # artworks may have many artists\n",
        "  artistids = w['Artist ID'].split(',')\n",
        "  aids = []\n",
        "  for aid in artistids:\n",
        "    try:\n",
        "      aids.append(int(aid))\n",
        "    except:\n",
        "      pass\n",
        "\n",
        "  artworks.append(Artwork(int(w['Artwork ID']),\n",
        "                  w['Title'],\n",
        "                  aids,\n",
        "                  w['Name'],\n",
        "                  string2Date(w['Date']),\n",
        "                  w['Medium'],\n",
        "                  w['Dimensions'],\n",
        "                  string2Date(w['Acquisition Date']),\n",
        "                  w['Credit'],\n",
        "                  w['Catalogue'],\n",
        "                  w['Department'],\n",
        "                  w['Classification'],\n",
        "                  w['Object Number'],\n",
        "                  string2Float(w['Diameter (cm)']),\n",
        "                  string2Float(w['Circumference (cm)']),\n",
        "                  string2Float(w['Height (cm)']),\n",
        "                  string2Float(w['Length (cm)']),\n",
        "                  string2Float(w['Width (cm)']),\n",
        "                  string2Float(w['Depth (cm)']),\n",
        "                  string2Float(w['Weight (kg)']),\n",
        "                  string2Float(w['Duration (s)'])\n",
        "                  )\n",
        "  )"
      ],
      "metadata": {
        "id": "moSQ9vD7KXkT"
      },
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Sanity checks\n",
        "\n",
        "Are you getting reasonable results?\n",
        "\n",
        "1. Select an artist by id\n",
        "1. Get their artworks"
      ],
      "metadata": {
        "id": "Q8owCL8aZuCc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# sanity checks\n",
        "# select a random artist\n",
        "aid = random.randint(1,1000)\n",
        "me = artists[aid]\n",
        "\n",
        "myworks = me.getMyArtworks(artworks)\n",
        "worktitles = \"\\n - \".join([w.title for w in myworks])\n",
        "\n",
        "print(f\"My name is {me.name}, my gender is {me.gender}, and I am {me.nationality}.\")\n",
        "print(f\"MoMA collected {len(myworks)} of my works: \\n - {worktitles}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "etSGO6sfA8fY",
        "outputId": "4915924f-9a67-4a6e-9217-48522b467929"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "My name is Erich Buchegger, my gender is Male, and I am Austrian.\n",
            "MoMA collected 1 of my works: \n",
            " - The Record Corner in Magazingasse 1, Linz\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Cool, right? See the Wall Text exercise at the bottom when you're ready."
      ],
      "metadata": {
        "id": "cnmdsTjFwL_x"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Show the number of male vs. female for artists with specified gender"
      ],
      "metadata": {
        "id": "7yMZmJWdd4uI"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "genderSpecified = []\n",
        "\n",
        "for artist in artists:\n",
        "  if artist.gender:\n",
        "    genderSpecified.append(artist.gender)\n",
        "\n",
        "c = Counter(genderSpecified)\n",
        "\n",
        "d = donutplot(\n",
        "    list(c.keys()),\n",
        "    list(c.values()),\n",
        "    legend=f\"Gender of {len(genderSpecified):,} artists with specified gender\")\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 497
        },
        "id": "FQg_F1igyKV6",
        "outputId": "7b822932-44b5-4ccd-b82b-de5f19cd6756"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 768x576 with 1 Axes>"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Explore the missing data\n",
        "\n",
        "1. Count how many artists are missing entries for name, gender, nationality, birth, and death.\n",
        "1. Profile the missing data by displaying 100 rows."
      ],
      "metadata": {
        "id": "w8dTs1Kkhtey"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "noGender = [a.id for a in artists if a.gender == '']\n",
        "noNationality = [a.id for a in artists if a.nationality == None]\n",
        "\n",
        "print(f\"{len(noGender):,} artists have unspecified gender.\")\n",
        "print(f\"{len(noNationality):,} artists have unspecified nationality\")\n",
        "print()\n",
        "\n",
        "# Start here\n",
        "noName = []\n",
        "noBirth = []\n",
        "noDeath = []\n",
        "\n",
        "print(\"Get these values:\")\n",
        "print(f\"{len(noName):,} artists have no name.\")\n",
        "print(f\"{len(noBirth):,} artists have no birth year.\")\n",
        "print(f\"{len(noDeath):,} artists have no death year.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kEGPwmRi0kvX",
        "outputId": "d2f39502-3c96-4747-ea42-3e9ddd943d86"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3,072 artists have unspecified gender.\n",
            "2,488 artists have unspecified nationality\n",
            "\n",
            "Get these values:\n",
            "0 artists have no name.\n",
            "0 artists have no birth year.\n",
            "0 artists have no death year.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Plot their nationalities\n",
        "\n",
        "Can you think of a more expressive plot for the data?"
      ],
      "metadata": {
        "id": "u9Qdnzg2wbz_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# What are their nationalities?\n",
        "\n",
        "c = Counter( [n.nationality for n in artists] )\n",
        "\n",
        "nations = [n for n, counte in c.items() if counte >= 500]\n",
        "counts = [counte for n, counte in c.items() if counte >= 500]\n",
        "\n",
        "d = donutplot(\n",
        "    list(nations),\n",
        "    list(counts),\n",
        "    legend=f\"Top Nationalities of the {len(vital):,} artists collected by MoMA\")\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 240
        },
        "id": "M6w7F2M5vORZ",
        "outputId": "88bcc69b-b5e1-410a-a662-9d785a33254d"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-11-f5e0b3df192f>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      9\u001b[0m     \u001b[0mlist\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnations\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     10\u001b[0m     \u001b[0mlist\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcounts\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 11\u001b[0;31m     legend=f\"Top Nationalities of the {len(vital):,} artists collected by MoMA\")\n\u001b[0m\u001b[1;32m     12\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     13\u001b[0m \u001b[0mplt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mshow\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'vital' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Create a function that will print wall text for an artwork. Include:\n",
        "\n",
        "- Title\n",
        "- Artist(s)\n",
        "- Date\n",
        "- Medium\n",
        "- Dimensions\n",
        "- Acquisition Date\n",
        "\n",
        "## Example:\n",
        "\n",
        "```\n",
        "Plate (folio 15) from BIOTHERM, 1989\n",
        "By Jim Dine\n",
        "Medium: \n",
        "Dimensions: irreg. composition  21 7/16 x 13 3/4\" (54.5 x 35 cm)\n",
        "```"
      ],
      "metadata": {
        "id": "xzO8xrxmnBHg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Create a function that will print walltext for a randomly seelcted artwork\n",
        "awid = random.randint(1,10000)\n",
        "showme = artworks[awid]\n",
        "\n",
        "# Display relevant info. Here's a hint!\n",
        "print(f\"{showme.title} | {showme.date:%Y}\")\n",
        "\n",
        "print(\"Help, I need names!\")\n",
        "\n",
        "# How will you get the artists names?"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UjAHuc2MmlZe",
        "outputId": "3fd3dcf5-d541-414c-ccf9-3d58f5f04b69"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Plate (folio 14 verso) from THE CÔTE D'AZUR TRIANGLE | 1985\n",
            "Help, I need names!\n"
          ]
        }
      ]
    }
  ]
}