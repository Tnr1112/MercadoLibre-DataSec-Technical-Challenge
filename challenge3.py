import os
import mysql.connector


def getMySqlConnection():
	mysqlConnection = mysql.connector.connect(
		host     = os.getenv('MYSQL_HOST'),
		user     = os.getenv('MYSQL_USER'),
		password = os.getenv('MYSQL_PASSWORD'),
		database = os.getenv('MYSQL_DATABASE')
	)

	return mysqlConnection

def getCustomersWithFailures(mySqlConnection):
	cursor = mySqlConnection.cursor()

	cursor.execute('''
						SELECT
								CONCAT(cust.first_name, ' ', cust.last_name) AS 'customer',
								COUNT(e.status) AS 'failures'
						FROM customers as cust
						INNER JOIN campaigns as camp ON cust.id = camp.customer_id
						INNER JOIN events as e ON camp.id = e.campaign_id
						WHERE e.status = "failure"
						GROUP BY customer
						HAVING failures > 3
					''')

	return cursor.fetchall()

def main():
	mySqlConnection = getMySqlConnection()
	print(getCustomersWithFailures(mySqlConnection))

if __name__ == '__main__':
	main()