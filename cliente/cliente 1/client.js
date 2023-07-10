// Define la URL del servidor
const serverURL = 'http://localhost:8001';

// Variables globales
let products = []; // Almacena la lista de productos
let editingProductId = null; // Almacena el ID del producto en edición

// Función para crear un producto
function createProduct(event) {
  event.preventDefault();
  
  const id = document.getElementById('id').value;
  const name = document.getElementById('name').value;
  const value = document.getElementById('value').value;
  
  fetch(`${serverURL}/products`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({id, name, value})
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);
    alert(data.message);
    fetchProducts();
  })
  .catch(error => console.error(error));
}

// Función para obtener la lista de productos
function fetchProducts() {
  fetch(`${serverURL}/products`)
  .then(response => response.json())
  .then(data => {
    products = data; // Almacenar la lista de productos
    
    const productsList = document.getElementById('products-list');
    productsList.innerHTML = ''; // Limpiar la lista antes de volver a mostrar los productos
    
    products.forEach(product => {
      const row = document.createElement('tr');
      
      const idCell = document.createElement('td');
      idCell.textContent = product.id;
      row.appendChild(idCell);
      
      const nameCell = document.createElement('td');
      nameCell.textContent = product.name;
      row.appendChild(nameCell);
      
      const valueCell = document.createElement('td');
      valueCell.textContent = product.value;
      row.appendChild(valueCell);
      
      const actionsCell = document.createElement('td');
      
      const editButton = document.createElement('button');
      editButton.textContent = 'Editar';
      editButton.addEventListener('click', () => editProduct(product.id));
      actionsCell.appendChild(editButton);
      
      const deleteButton = document.createElement('button');
      deleteButton.textContent = 'Eliminar';
      deleteButton.addEventListener('click', () => deleteProduct(product.id));
      actionsCell.appendChild(deleteButton);
      
      row.appendChild(actionsCell);
      
      productsList.appendChild(row);
    });
  })
  .catch(error => console.error(error));
}

// Función para editar un producto
function editProduct(productId) {
  // Buscar el producto correspondiente en la lista
  const product = products.find(p => p.id === productId);
  
  // Llenar los campos del formulario con los datos del producto
  document.getElementById('id').value = product.id;
  document.getElementById('name').value = product.name;
  document.getElementById('value').value = product.value;
  
  // Guardar el ID del producto en edición
  editingProductId = productId;
  
  // Cambiar el texto y el evento del botón de "Enviar"
  const submitButton = document.querySelector('#create-form input[type="submit"]');
  submitButton.value = 'Actualizar';
  submitButton.removeEventListener('click', createProduct);
  submitButton.addEventListener('click', updateProduct);
}

// Función para actualizar un producto
function updateProduct(event) {
  event.preventDefault();
  
  const id = document.getElementById('id').value;
  const name = document.getElementById('name').value;
  const value = document.getElementById('value').value;
  
  fetch(`${serverURL}/products/${editingProductId}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({id, name, value})
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);
    alert(data.message);
    fetchProducts();
  })
  .catch(error => console.error(error));
  
  // Restaurar el formulario y el botón de "Enviar" a su estado original
  document.getElementById('create-form').reset();
  const submitButton = document.querySelector('#create-form input[type="submit"]');
  submitButton.value = 'Enviar';
  submitButton.removeEventListener('click', updateProduct);
  submitButton.addEventListener('click', createProduct);
  
  // Limpiar el ID del producto en edición
  editingProductId = null;
}

// Función para eliminar un producto
function deleteProduct(productId) {
  // Aquí puedes implementar la lógica para eliminar un producto
  alert(`Eliminar producto con ID: ${productId}`);
}

// Event listener para enviar el formulario de creación de producto
document.getElementById('create-form').addEventListener('submit', createProduct);

// Obtener la lista de productos al cargar la página
fetchProducts();
