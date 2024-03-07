### ?? 안에 뭐가 들어가야 3번째 문장이 빨간색이 되는지

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        div ?? span {
        color: red;
        }
    </style>
</head>
<body>
      
    <div>
        <h1>내가 집에 가고 싶은 이유</h1>
        <p>
            <span>피곤하기 때문에</span>
        </p>
        <div>
            <span>집에서 공부하면 효율이 더 좋아서 집가서 더 공부할거임</span>
        </div>
    </div>
</body>
</html>
```

### ??에 뭐가 들어가야 노란색이 되는지

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .yellow {
            color: yellow ??;
        }
        
        #brown{
            color: brown;
        }
    </style>
</head>
<body>
    <span class="yellow" id="brown">독수리 부리는 왜 노랄까?</span>
</body>
</html>
```

### 노랗게 만들려면 ??에 뭐가 들어가야 할지

```
<style>
    h1 {
        ??: yellow;
    }
</style>

<body>
    <h1>독수리 부리는 왜 노랄까?</h1>
</body>
```

### 리스트의 종류 구분(단답)

- ul

- ol

- li

### 색이 어떨게 될지 색깔과 그 이유(서술)

```
<style>
    .blue {
      color: blue;
    }
    .red {
      color: red;
    }
</style>

<div class="blue red">Hello</div>
<div class="red blue">World</div>
```