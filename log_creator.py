#!/usr/bin/env python3

import psycopg2

DBNAME = "news"


def print_top_three_ever():
    db = psycopg2.connect(dbname=DBNAME)
    c = db.cursor()
    c.execute("select title, num \
        from articles join (create or replace view status_ok as \
        select overlay(path placing '' from 1 for 9) as slug, \
        count(*) as num \
        from log \
        where status like '%200%' \
        group by path order by num desc) as status_ok \
        on articles.slug = status_ok.slug \
        limit 3")
    results = c.fetchall()
    for res in results:
        print("* " + res[0] + " - " + str(res[1]) + " views.")
    db.close()


def print_top_authors_ever():
    db = psycopg2.connect(dbname=DBNAME)
    c = db.cursor()
    c.execute("select name, views \
        from authors join \
        (select author as id, sum(num::int) as views \
        from articles join (create or replace view status_ok as \
        select overlay(path placing '' from 1 for 9) as slug, \
        count(*) as num \
        from log \
        where status like '%200%' \
        group by path order by num desc) as status_ok \
        on articles.slug = status_ok.slug \
        group by author \
        order by views desc) as view_counter\
        on view_counter.id = authors.id")
    results = c.fetchall()
    for res in results:
        print("* " + res[0] + " - " + str(res[1]) + " views.")
    db.close()


def print_when_had_more_errors():
    db = psycopg2.connect(dbname=DBNAME)
    c = db.cursor()
    c.execute("select date, percentual from (select errors.date, \
        (total_errors::decimal / total_logs::decimal * 100) as percentual\
        from (select time::date as date, count(*) as total_errors \
        from log where status like '%404%' \
        group by date) as errors join \
        (select time::date as date, count(*) as total_logs \
        from log group by date) as all_logs \
        on errors.date = all_logs.date \
        order by percentual desc) as resume \
        where percentual > 1")
    results = c.fetchall()
    for res in results:
        print(
            "* " + res[0].strftime("%B %d, %Y") + " - " +
            str(round(res[1], 2)) + "% errors"
        )
    db.close()


print('\n1. What are the three most popular articles of all time?')
print_top_three_ever()

print('\n2. Who are the authors of most popular articles of all time?')
print_top_authors_ever()

print('\n3. On what days more than 1% of requests resulted in errors?')
print_when_had_more_errors()
