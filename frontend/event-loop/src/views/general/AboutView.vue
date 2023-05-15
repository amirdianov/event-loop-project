<template>
    <div class="about-page">
        <div class="hero-section">
            <h2>О нашей платформе</h2>
            <p style="font-size: 1.3rem">Наша платформа объединяет людей, позволяя им делиться знаниями, навыками и весело проводить время в кругу
                единомышленников.</p>
        </div>
        <div class="content-section">
            <div class="info-block">
                <h3>Станьте организатором</h3>
                <p>Создавайте свои собственные мероприятия с подробными описаниями, устанавливайте даты, места и, при
                    необходимости, взимайте плату. Отслеживайте регистрации, читайте отзывы и отправляйте уведомления
                    участникам. Удивляйте их особыми сюрпризами!</p>
            </div>
            <div class="info-block">
                <h3>Наша целевая аудитория</h3>
                <p>Мы приветствуем людей, которые любят общаться, делиться идеями и исследовать новые впечатления. Будь
                    вы заинтересованы в организации мероприятий или их посещении, наша платформа предлагает что-то для
                    каждого.</p>
            </div>
            <div class="info-block">
                <h3>Проблема и решение</h3>
                <p>В мире, где социальные взаимодействия уменьшаются, мы предоставляем решение. Наша платформа
                    способствует налаживанию значимых связей, поощряя организацию и участие в мероприятиях. Переоткройте
                    радость общения с другими людьми, разделяющими ваши интересы.</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "AboutPage",
};
</script>

<style scoped>
.about-page {
    max-width: 100%;
    margin: 0 auto;
}

.hero-section {
    text-align: center;
    margin-bottom: 3rem;
}

h1 {
    font-size: 5rem;
    margin-bottom: 1rem;
}

p {
    font-size: 1.1rem;
    line-height: 2rem;
    margin-bottom: 1.5rem;
}

.content-section {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 2rem;
}

.info-block {
    background-color: #f5f5f5;
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: background-color 0.3s ease-in-out;
}

.info-block:hover {
    background-color: #976f4f;
}

h2 {
    font-size: 3rem;
    margin-bottom: 1rem;
}

h3 {
    font-size: 1.25rem;
    margin-bottom: 1rem;
}

.info-block:hover h2,
.info-block:hover h3 {
    color: #ffffff;
}

.info-block:hover p {
    color: #ffffff;
}

@media (max-width: 900px) {
    .content-section {
        grid-template-columns: 1fr;
    }
}
</style>