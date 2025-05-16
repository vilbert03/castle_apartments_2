
document.addEventListener("DOMContentLoaded", function () {
    function registerSearchButtonHandler() {
        const searchButton = document.getElementById("search-icon");
        const searchValueElement = document.getElementById("search-value");
        const propertyPlaceholder = document.getElementById("property-results");

        searchButton.addEventListener("click", async function () {
            const value = searchValueElement.value;

            const response = await fetch(`?search_filter=${encodeURIComponent(value)}`);
            if (response.ok) {
                const json = await response.json();
                const properties = json.data;

                propertyPlaceholder.innerHTML = properties.map(property => `
                    <div class="property-item">
                        <h3>${property.name}</h3>
                        <div class="property-image" style="background-image: url(${property.image})"></div>
                        <div class="property-type">${property.type}</div>
                        <div class="property-price">${property.price} ISK</div>
                        <a href="/Property/${property.id}">More details</a>
                    </div>
                `).join('');
            }
        });
    }

    registerSearchButtonHandler();
});
