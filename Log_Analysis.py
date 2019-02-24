#!/usr/bin/env python2
import psycopg2
import datetime


DBNAME = 'news'


def popular_article():
    """Return the three most popular articles of all time"""
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute("""
            SELECT articles.title, count(*) AS views
            FROM articles JOIN log
            ON log.path LIKE '%' || articles.slug
            GROUP BY articles.title
            ORDER BY views desc
            LIMIT 3
            """)
        pop_article = c.fetchall()
        db.close()
        # Formating the table
        for row in pop_article:
            print '"{}" - {} views' .format(row[0], row[1])
    except:
        print 'Unable to connect to the database'


def popular_author():
    """Return the most popular article authors of all time"""
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute("""
            SELECT aut_art.name, count(*) AS views
            FROM (authors join articles
            ON authors.id = articles.author) AS aut_art JOIN log
            ON log.path like '%' || aut_art.slug
            GROUP BY aut_art.name
            ORDER BY views desc;
            """)
        pop_author = c.fetchall()
        db.close()
        # Formating the table
        for row in pop_author:
            print '"{}" - {} views' .format(row[0], row[1])
    except:
        print 'Unable to connect to the database'


def requests_errors():
    """Return days with more than 1% of requests errors"""
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute("""
            SELECT date_trunc('day', time) AS date,
            COUNT(status) FILTER (where status = '200 OK') AS sucesses,
            COUNT(status) FILTER (where status != '200 OK')  AS errors
            FROM log
            GROUP BY date
            ORDER BY date""")
        requests = c.fetchall()
        db.close()
        # Formatin the table
        for row in requests:
            total = row[1] + row[2]
            errors = ((row[2] * 100.0) / total)
            if errors > 1:
                print '{} - {:.2f}% errors' .format(row[0].strftime('%b %d %Y'),
                                                errors)
    except:
        print 'Unable to connect to the database'


# Call the functions and format it to display
print 'The three most popular articles of all time \n'
popular_article()
print ''
print 'The most popular article authors of all time \n'
popular_author()
print ''
print 'Days with more than 1% of requests errors \n'
requests_errors()
