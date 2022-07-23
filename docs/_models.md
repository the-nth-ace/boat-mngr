# 🚤 Boat Manager

## 🗜 Models

1. ### Business
    ```smalltalk
   - Business name
   - Operation commence time
   - Owner Name
   - Total boats [Model] - Calculated from Boat?
    ```


3. ### Boat
    ```smalltalk
   - Boat Name
   - Capacity
   - Captain Name
   - Captain Picture
   - Deckhand Name
   - Review [Model] [ 1 - * ]
   - Business [Model] [ * - 1 ]
   - Average Rating [Model] - Calculated from Reviews
    ```

4. #### Review
    ```smalltalk
      - Reviewer Name?
      - Boat [Model]
      - Rating [Min 1, Max 5]
      - Review [Actual Review, Optional] 
      - DateTimeAdded [for sorting purposes]
     ```

5. ### User Models
    Customers do not require Accounts so that leaves just PRO and the Admin. In terms of authentication, which can be interpreted as:

    - PRO - Manager vibe with administrative rights
    - Admin - Admin

    1. #### PRO
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


