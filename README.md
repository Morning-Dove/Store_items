A small api to list store items

**Store Items**

Attributes:

* id (int)
* name (string)
* description (string)
* price (float)


## REST Endpoints

Name                           | Method | Path
-------------------------------|--------|------------------
Retrieve store_items collection| GET    | /store_items
Create store_items member      | POST   | /store_items
Update store_items member      | PUT    | /store_items/*\<item_id\>*
Delete store_items member      | DELETE | /store_items/*\<item_id\>*