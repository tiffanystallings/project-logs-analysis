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
My virtual machine was built using Vagrant and VirtualBox, utilizing Udacity's preset vagrant machine. You can get more information on their VM from [here](https://github.com/udacity/fullstack-nanodegree-vm)

With your virtual machine set up (if preferred) and PostgreSQL installed, you can proceed with initializing the database.

In your command line, enter:
`psql -d news -f newsdata.sql`

Once the News Database is initialized, open the database by entering:
`psql news`

### Creating Required Views
Aggregator.py depends on three views to function. Create them by opening the database in the command line and entering:
```
create view top_articles as
select title, count(articles.slug) as views
from articles, log
where articles.slug = substring(log.path from 10 for char_length(log.path))
group by articles.title
order by views desc;
```

```
create view top_authors as
select name, count(articles.slug) as views
from authors, articles, log
where articles.slug = substring(log.path from 10 for char_length(log.path))
and authors.id = articles.author
group by authors.name
order by views desc;
```

```
create view high_errors as
select date, round(num*100.0/total, 2) as percent
from (
select date(log.time) as date, count(log.time) as total, sub.num
from log
left join
	(select date(log.time) as date, count(log.time) as num
	 from log
	 where status like '4%'
	 or status like '5%'
	 group by date(log.time)
	) as sub
on date(log.time)=sub.date
group by date(log.time), sub.num) as calculated
where num*1.0/total > 0.01;
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
This project was built as part of Udacity's Full Stack Web Developer Nanodegree. It would be in violation of the honor code for me to accept any direct contributions to the code.

However, if you have any advice or suggestions on how I might improve the code, please feel free to take out an Issue on the project's [github](https://github.com/tiffanystallings/project-logs-analysis).

