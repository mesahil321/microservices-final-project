Feature: Product Management

  Background:
    Given the following products exist
      | name     | category | price | available |
      | WidgetA  | Tools    | 10.99 | true      |
      | GadgetB  | Gadgets  | 25.50 | false     |

  Scenario: Read a product
    When I request the product with name "WidgetA"
    Then I should receive the product details with name "WidgetA"

  Scenario: Update a product
    When I update the product "WidgetA" with new price 12.99
    Then the product "WidgetA" should have price 12.99

  Scenario: Delete a product
    When I delete the product with name "GadgetB"
    Then the product "GadgetB" should not exist

  Scenario: List all products
    When I request all products
    Then I should receive a list of all products

  Scenario: Search products by name
    When I search products by name "WidgetA"
    Then I should receive products with name "WidgetA"

  Scenario: Search products by category
    When I search products by category "Tools"
    Then I should receive products in category "Tools"

  Scenario: Search products by availability
    When I search products by availability "true"
    Then I should receive products where availability is true
