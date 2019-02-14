from behave import when, then, given

from customer_service.model.customer import Customer


@given('customer "{name}" with ID "{customer_id:d}" exists')
def create_customer(context, name, customer_id):
    (first_name, surname) = name.split(' ', 2)

    customer = Customer(customer_id=customer_id,
                        first_name=first_name,
                        surname=surname)

    context.customer_repository.store(customer)


@given('there is no customer with ID "99999"')
def do_not_create_customer(context):
    pass  # Intentionally blank


@when('I fetch customer "{customer_id}"')
def fetch_customer(context, customer_id):
    context.response = context.web_client.get(f'/customers/{customer_id}')


@then('I should see customer "{expected_name}"')
def assert_customer(context, expected_name):
    response = context.response

    assert response.status_code == 200, response.status_code
    assert response.is_json
    body = response.get_json()
    assert f"{body['firstName']} {body['surname']}" == expected_name


@then("I should get a not found response")
def assert_not_found_response(context):
    assert context.response.status_code == 404, context.response.status_code


@when(u'customer "{customer_id}" surname is updated to "{new_surname}"')
def assert_surname_updated(context, customer_id, new_surname):
    response = context.web_client.post(
        '/customers/update',
        json={'customer_id': customer_id, 'surname': new_surname})

    assert response.status_code == 200, response.status_code


@then(u'customer "{customer_id}" surname is changed to "{surname}"')
def name_is_updated(context, customer_id, surname):
    response = context.web_client.get(f'/customers/{customer_id}')

    assert response.status_code == 200, response.status_code

    assert response.is_json
    body = response.get_json()
    assert body['surname'] == surname, \
        f"'{body['surname']}' not equals '{surname}'"
