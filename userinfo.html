function getUserIdFromUrl() {
    const params = new URLSearchParams(window.location.search);
    return params.get('userid');
}

async function fetchRobloxUserInfo(userId) {
    const response = await fetch(`https://users.roblox.com/v1/users/${userId}`);
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.json();
}

function displayUserInfo(userInfo) {
    const output = document.getElementById('output');
    output.innerHTML = `
        <h2>User Information</h2>
        <p><strong>Username:</strong> ${userInfo.name}</p>
        <p><strong>User ID:</strong> ${userInfo.id}</p>
        <p><strong>Description:</strong> ${userInfo.description}</p>
        <p><strong>Created:</strong> ${new Date(userInfo.created).toLocaleString()}</p>
    `;
}

function displayError(error) {
    const output = document.getElementById('output');
    output.innerHTML = `<p>Error: ${error.message}</p>`;
}

async function main() {
    const userId = getUserIdFromUrl();
    if (!userId) {
        displayError(new Error('User ID not provided in URL'));
        return;
    }

    try {
        const userInfo = await fetchRobloxUserInfo(userId);
        displayUserInfo(userInfo);
    } catch (error) {
        displayError(error);
    }
}

main();
