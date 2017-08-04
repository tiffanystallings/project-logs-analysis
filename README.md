# News Database Analysis

A simple Python script that utilizes a DB API to pull data from a local news database.

## Installation

Using Git Bash:  
`$ git clone https://github.com/tiffanystallings/project-logs-analysis.git`

From a ZIP:  
1. Visit the project's github [here](https://github.com/tiffanystallings/project-logs-analysis)
2. Click the **Clone or Download** dropdown box and select  
**Download ZIP**.
3. Open the ZIP and click **Extract All**. Select your preferred  folder and hit **Extract**.

## Requirements
* [Python 3](https://www.python.org/downloads/)
* Python Module - psycopg2
* [PostgreSQL](https://www.postgresql.org/download/)
* The SQL News database provided by Udacity

Optional:
* [Vagrant](https://www.vagrantup.com/downloads.html)
* [Oracle VirtualBox VM](https://www.virtualbox.org/wiki/Downloads)

## Setup
### Installing psycopg2
With Python3 installed, open your preferred comand line interface and enter:
`pip install pyscopg2`

### Initializing the Database
With PostgreSQL installed, open your preferred command line interface (or a virtual machine using Vagrant and VirtualBox) and navigate to the project-logs-analysis directory.

To initialize the database, enter:
`psql -d news -f newsdata.sql`

Once the News Database is initialized, open the database by entering:
`psql news`

## Usage

## Contributions

