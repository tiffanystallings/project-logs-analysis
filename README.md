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
* Custom Views - Created in Setup below

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

### Creating Required Views
Aggregator.py depends on three views to function. Create them by opening the database in the command line and entering:
```

```

```

```

```

```

## Usage
From the Command Line:
With Python installed and all prior setup completed, open your preferred command line and navigate to the project-logs-analysis directory.
Enter:
`python aggregator.py`

From IDLE:
(With all prior setup completed)
1. Open IDLE(Python 3._x_._x_)
2. Select File -> Open...
3. Navigate to the directory where project-logs-analysis is installed and open aggregator.py.
4. A new window for aggregator.py will open. From that  window, select Run -> Run Module.
5. The code should output to the IDLE shell.

## Contributions

