# 🚤 Boat Manager

## 🗜 Models

1. ### Business
    ```smalltalk
   - Name
   - Owner [Model] User Model or Derivative | ][ 1-1 OR * - 1 ]
    ```


3. ### Boat
    ```smalltalk
   - Name?
   - Capacity?
   - Boat Photo
   - Captain Name
   - Captain Picture
   - Review [Model] [ 1 - * ]
   - Business [Model] [ * - 1 ]
   - Average Rating [Model] - Calculated from Reviews
    ```

4. #### Review
    ```smalltalk
      - Reviewer Name?
      - Boat [Model]
      - Rating [Min 1, Max 5]
      - Review [Actual Review, Optional?] 
      - DateTimeAdded [for sorting purposes]
     ```

5. ### User Models
    Customers do not require Accounts so that leaves just Owners and the Admin. In terms of authentication, which can be interpreted as:

    - Owner - Regular Users
    - Admin - Admin

    1. #### Owner
         ```smalltalk  
        - Username?
        - Email?
        - Password
        - Busines[Model] [ 1 - * ]
        - User[Model] [ 1 - 1 ]
        ```
    1. #### Admin
        ```smalltalk
        - Username?
        - Email?
        - Password
        ```


