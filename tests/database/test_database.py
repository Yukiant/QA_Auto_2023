import pytest
from modules.common.database import Database
import datetime as dt


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()
    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name("Sergii")
    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)
    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, "печиво", "солодке", 30)
    water_qnt = db.select_product_qnt_by_id(4)
    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, "тестові", "дані", "999")
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)
    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    assert len(orders) == 1
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"


# Below there are tests created within the individual homework


# 1
@pytest.mark.dbind
def test_corrupted_primary_key():
    """Check that it is impossible to add a new data row with wrong data type for the primary key (not integer)"""
    db = Database()
    result = db.insert_customers("not_integer_key", "Petro", "Street 1", "Kiyv", "01000", "Ukraine")
    assert result == False


# 2
@pytest.mark.dbind
def test_no_nulls():
    """Check that all entries do not have NULL values in all tables"""
    db = Database()
    result1 = db.get_null_entries_customers()
    result2 = db.get_null_entries_products()
    result3 = db.get_null_entries_orders()
    assert result1 == []
    assert result2 == []
    assert result3 == []


# 3
@pytest.mark.dbind
def test_Sergii_order():
    """Check that customer Sergii made exactly 1 order"""
    db = Database()
    result = db.get_orders("Sergii")
    assert len(result) == 1


# 4
@pytest.mark.dbind
def test_no_orders_Stepan():
    """Check that customer Stepan did not make any orders at all"""
    db = Database()
    result = db.get_orders("Stepan")
    assert len(result) == 0


# 5
@pytest.mark.dbind
def test_no_orders_Stepan_alternative():
    """
    Check that customer Stepan did not make any orders at all
    This is another approach to the test #4 above - using LEFT JOIN
    """
    db = Database()
    result = db.get_info_no_orders()
    assert result[0][1] == "Stepan"


# 6
@pytest.mark.dbind
def test_ukrainian_customers():
    """Check that exactly two customers live in Ukraine"""
    db = Database()
    result = db.get_customer_by_parameter("country", "Ukraine")
    assert len(result) == 2


# 7
@pytest.mark.dbind
def test_ukrainian_customers__alternative():
    """
    Check that exactly two customers live in Ukraine
    Second approach to the above test - using SQL COUNT
    """
    db = Database()
    result = db.count_customers_by_country("Ukraine")
    assert result[0][0] == 2


# 8
@pytest.mark.dbind
def test_stock():
    """Check that stock of product "печиво" is the biggest"""
    db = Database()
    result = db.get_maximal_stock()
    assert result[0][0] == "печиво"


# 9
@pytest.mark.dbind
def test_order_date():
    """Check that order_date (time) for the orders of customer Sergii is later than 12:00:00"""
    check_time = dt.time(12, 0, 0)
    db = Database()
    result = db.get_orders("Sergii")
    result_order_date = [
        True
        if dt.datetime.strptime(entry[3], "%H:%M:%S").time() > check_time
        else False
        for entry in result
    ]
    assert all(result_order_date) == True


# 10
@pytest.mark.dbind
def test_stock_more_entries():
    """
    Check that order_date (time) for the orders of customer Sergii is later than 12:00:00
    This is the same test as above #9. A few more entries are added to the table orders to see processing of more data.
    """
    check_time = dt.time(12, 0, 0)
    db = Database()

    # Adding a few more entries to orders table:

    db.insert_orders(2, 1, 2, "13:30:00")
    db.insert_orders(3, 1, 3, "14:30:04")
    db.insert_orders(4, 2, 2, "15:45:24")

    # Test itself:

    result = db.get_orders("Sergii")
    result_order_date = [True if dt.datetime.strptime(entry[3], "%H:%M:%S").time() > check_time else False for entry in result]
    assert all(result_order_date) == True

    # Remove extra test entries:

    for id in [2, 3, 4]:
        db.delete_order(id)
