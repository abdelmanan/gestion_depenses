const API_URL = "http://127.0.0.1:8000";

const form = document.getElementById("expense-form");
const expensesList = document.getElementById("expenses-list");
const totalElement = document.getElementById("total");
const messageElement = document.getElementById("message");


// ========================================
// Récupérer toutes les dépenses
// ========================================

async function loadExpenses() {

    try {

        const response = await fetch(
            API_URL + "/expenses"
        );

        if (!response.ok) {

            throw new Error(
                "Impossible de récupérer les dépenses."
            );
        }

        const expenses = await response.json();

        displayExpenses(expenses);

        await loadTotal();

    } catch (error) {

        console.error(error);

        messageElement.textContent =
            error.message;
    }
}


// ========================================
// Afficher les dépenses
// ========================================

function displayExpenses(expenses) {

    expensesList.innerHTML = "";


    if (expenses.length === 0) {

        expensesList.textContent =
            "Aucune dépense enregistrée.";

        return;
    }


    expenses.forEach(function(expense) {

        const element =
            document.createElement("div");

        element.classList.add("expense");


        const info =
            document.createElement("div");

        info.classList.add("expense-info");


        const description =
            document.createElement("strong");

        description.textContent =
            expense.description;


        const category =
            document.createElement("span");

        category.textContent =
            "Catégorie : " + expense.category;


        const details =
            document.createElement("span");

        details.textContent =
            Number(expense.amount).toFixed(2)
            + " DH - "
            + expense.expense_date;


        info.appendChild(description);
        info.appendChild(category);
        info.appendChild(details);


        const deleteButton =
            document.createElement("button");

        deleteButton.textContent =
            "Supprimer";

        deleteButton.classList.add(
            "delete-button"
        );


        deleteButton.addEventListener(
            "click",
            function() {

                deleteExpense(expense.id);

            }
        );


        element.appendChild(info);
        element.appendChild(deleteButton);


        expensesList.appendChild(element);

    });
}


// ========================================
// Récupérer le total
// ========================================

async function loadTotal() {

    const response = await fetch(
        API_URL + "/expenses/total"
    );


    if (!response.ok) {

        throw new Error(
            "Impossible de récupérer le total."
        );
    }


    const data =
        await response.json();


    totalElement.textContent =
        Number(data.total).toFixed(2);
}


// ========================================
// Ajouter une dépense
// ========================================

form.addEventListener(
    "submit",
    async function(event) {

        event.preventDefault();


        const description =
            document
                .getElementById("description")
                .value
                .trim();


        const amount =
            parseFloat(
                document
                    .getElementById("amount")
                    .value
            );


        const category =
            document
                .getElementById("category")
                .value
                .trim();


        const expenseDate =
            document
                .getElementById("expense-date")
                .value;


        const expense = {

            description: description,

            amount: amount,

            category: category,

            expense_date: expenseDate

        };


        try {

            const response = await fetch(
                API_URL + "/expenses",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify(expense)
                }
            );


            if (!response.ok) {

                const errorData =
                    await response.json();


                throw new Error(
                    errorData.detail ||
                    "Erreur lors de l'ajout."
                );
            }


            form.reset();


            messageElement.textContent =
                "Dépense ajoutée avec succès.";


            await loadExpenses();


        } catch (error) {

            console.error(error);

            messageElement.textContent =
                error.message;
        }

    }
);


// ========================================
// Supprimer une dépense
// ========================================

async function deleteExpense(id) {

    try {

        const response = await fetch(
            API_URL + "/expenses/" + id,
            {
                method: "DELETE"
            }
        );


        if (!response.ok) {

            const errorData =
                await response.json();


            throw new Error(
                errorData.detail ||
                "Impossible de supprimer la dépense."
            );
        }


        messageElement.textContent =
            "Dépense supprimée avec succès.";


        await loadExpenses();


    } catch (error) {

        console.error(error);

        messageElement.textContent =
            error.message;
    }
}


// ========================================
// Démarrage de l'application
// ========================================

loadExpenses();