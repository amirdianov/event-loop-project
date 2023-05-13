<template>
    <div class="container">
        <img src="@/assets/images/logo3.0.png" width="700" height="157"
             alt="Логотип">
        <h1 class="title">Добро пожаловать на наш сайт!</h1>
        <h2 class="subtitle">Здесь вы найдете много интересного</h2>

    </div>
</template>

<style>
.container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 550px;
    background-color: #f5f5f5;
}

.title {
    font-size: 4rem;
    font-weight: bold;
    color: #976f4f;
    margin-bottom: 0.5rem;
}

.subtitle {
    font-size: 2rem;
    font-weight: bold;
    color: #976f4f;
    margin-bottom: 1rem;
}

.description {
    font-size: 1.5rem;
    color: #333;
    max-width: 500px;
    text-align: center;
    margin-bottom: 2rem;
}

.title:hover {
    animation: shake 0.5s;
}

@keyframes shake {
    0% {
        transform: translateX(0);
    }
    25% {
        transform: translateX(-5px);
    }
    50% {
        transform: translateX(5px);
    }
    75% {
        transform: translateX(-5px);
    }
    100% {
        transform: translateX(0);
    }
}
</style>
