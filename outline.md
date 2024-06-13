
accounts

contact

home

login
#################

- Device:
    pc:      
        Device code
        Device type[(Pc), (Laptop), (Monitpr), (Printer)]
        Model name
        Motherboard
        Cpu
        Ram
        Hdd
        Status[(New), (Used), (Damaged)]
        Site
        Price
        Other
 
    laptop:      
        Device code
        Device type[(Pc), (Laptop), (Monitpr), (Printer)]
        Model name
        Motherboard
        Cpu
        Ram
        Hdd
        Status[(New), (Used), (Damaged)]
        Site
        Price
        Other
 
    monitor      
        Device code
        Device type[(Pc), (Laptop), (Monitpr), (Printer)]
        Model name
        Status[(New), (Used), (Damaged)]
        Site
        Price
        Other

    printer      
        Device code
        Device type[(Pc), (Laptop), (Monitpr), (Printer)]
        Model name
        Status[(New), (Used), (Damaged)]
        Site
        Price
        Other

- Employee:
      Employee code
      Employee name
      Employee national id
      Birth date
      Employee phone 1
      Employee phone 2
      Governorate
      Employee email
      Image
      Slug

- Ticket:
    Title
    Description
    Requested by
    Assigned to
    Start date
    Due date
    Comment
    Status[(New), (In Progress), (Resolved), (Closed)])

-----------------
-url : path
-view : logic
-model : db
-templates : frontend

-----------------
Relations :
    - One to Many   [ User - Postes ]   Foreginkey
    - Many to Many  [ Admin - Groups ]   
    - One to One    [ User - Profile]

-----------------
** django model queryset
** django template language
**
