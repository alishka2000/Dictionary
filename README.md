URL: api/language-list                

```yaml
Method: 'GET'
```

This url gives us the all items we have in our table(JSON format)

For Example:
```yaml
id | name | id_default

1 |	"KZ" |	true

2 |	"RU" |	false

3 |	"ENG" |	false
```
After our query:

Give this result:
```yaml
[
    
{
        "id": 1,
        "code": "book",
        "name": "книга",
        "lang": 2
    },
    
{
        "id": 2,
        "code": "head",
        "name": "бас",
        "lang": 1
    },
    
{
        "id": 3,
        "code": "рука",
        "name": "arm",
        "lang": 3
    },
    
{
        "id": 5,
        "code": "foot",
        "name": "аяк",
        "lang": 1
    }

]
```

```yaml
URL: app/dictionary/
``` 

```yaml
Method: 'POST'
```

This url gives us chance to create item(we must write query by JSON)

For Example:

We write query like this:

```yaml
{
  "code": "finger",
  "name": "саусак",
  "lang": 1
}
```
and then it seems like :
```yaml
{
    "id": 7,
    "code": "finger",
    "name": "саусак",
    "lang": 1
}
```
```yaml
{
    "id": 7,
    "code": "finger",
    "name": "саусак",
    "lang": 1
}
```

URL: app/dictionary/<str:pk>/   
where: <str:pk>/ is 'id'

```yaml
Method: 'GET'
```

This url gives us only 1 item where 'id' is <str:pk>

For Example:

We write URL like this:
```yaml
api/dictionary/2
``` 

and choose method: "GET"

we take :
```yaml
{
    "id": 2,
    "code": "head",
    "name": "бас",
    "lang": 1
}
```

URL: app/dictionary/<str:pk>   
where: <str:pk> is 'id'

```yaml
Method: 'PUT'
```
This url can replace our item by the new one.(update by 'id')

For Example:

We write URL like this:
```yaml
api/dictionary/2 
```

and write in body:
```yaml
{
        "code": "test2",
        "name": "тест2",
        "lang": 1
}
```

and choose method: "PUT"

we take :
```yaml
{
    "id": 2,
    "code": "test2",
    "name": "тест2",
    "lang": 1
}
```

URL: app/dictionary/<str:pk>   
where: <str:pk> is 'id'
```yaml
Method: 'DELETE'
```

This method 'delete' item by 'id'

For Example:

We write URL like this:
```yaml
api/dictionary/2
```
 

and choose method: "DELETE"

we take :
```yaml
"Task Deleted Successfully"
```
