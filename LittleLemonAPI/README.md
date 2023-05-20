API Documentation for the Endpoints:

1. **Endpoint**: /menu-items/
   - **Method**: GET
   - **Description**: Retrieve a list of menu items.
   - **Response**:
     - 200 OK - Returns a list of menu items.
     - 401 Unauthorized - User authentication required.
     - 403 Forbidden - User does not have permission to access the resource.

2. **Endpoint**: /menu-items/{pk}/
   - **Method**: GET
   - **Description**: Retrieve details of a specific menu item.
   - **Parameters**:
     - {pk} (integer) - ID of the menu item.
   - **Response**:
     - 200 OK - Returns the details of the menu item.
     - 401 Unauthorized - User authentication required.
     - 403 Forbidden - User does not have permission to access the resource.
     - 404 Not Found - Menu item with the specified ID does not exist.

3. **Endpoint**: /groups/manager/users/
   - **Method**: GET
   - **Description**: Retrieve a list of managers' users.
   - **Response**:
     - 200 OK - Returns a list of managers' users.
     - 401 Unauthorized - User authentication required.
     - 403 Forbidden - User does not have permission to access the resource.

4. **Endpoint**: /groups/manager/users/{id}/
   - **Method**: GET
   - **Description**: Retrieve details of a specific manager's user.
   - **Parameters**:
     - {id} (integer) - ID of the manager's user.
   - **Response**:
     - 200 OK - Returns the details of the manager's user.
     - 401 Unauthorized - User authentication required.
     - 403 Forbidden - User does not have permission to access the resource.
     - 404 Not Found - Manager's user with the specified ID does not exist.

5. **Endpoint**: /groups/delivery-crew/users/
   - **Method**: GET
   - **Description**: Retrieve a list of delivery crew users.
   - **Response**:
     - 200 OK - Returns a list of delivery crew users.
     - 401 Unauthorized - User authentication required.
     - 403 Forbidden - User does not have permission to access the resource.

6. **Endpoint**: /groups/delivery-crew/users/{id}/
   - **Method**: GET
   - **Description**: Retrieve details of a specific delivery crew user.
   - **Parameters**:
     - {id} (integer) - ID of the delivery crew user.
   - **Response**:
     - 200 OK - Returns the details of the delivery crew user.
     - 401 Unauthorized - User authentication required.
     - 403 Forbidden - User does not have permission to access the resource.
     - 404 Not Found - Delivery crew user with the specified ID does not exist.

7. **Endpoint**: /cart/menu-items/
   - **Method**: GET
   - **Description**: Retrieve the items in the user's cart.
   - **Response**:
     - 200 OK - Returns the items in the user's cart.
     - 401 Unauthorized - User authentication required.
     - 403 Forbidden - User does not have permission to access the resource.

8. **Endpoint**: /orders/
   - **Method**: GET
   - **Description**: Retrieve a list of orders.
   - **Response**:
     - 200 OK - Returns a list of orders.
     - 401 Unauthorized - User authentication required.
     - 403 Forbidden - User does not have permission to access the resource.