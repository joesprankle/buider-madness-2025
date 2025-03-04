<template>
  <div class="min-h-screen bg-gray-900 text-gray-100 flex flex-col">
    <!-- Header with Logo and Sidebar Toggle Button -->
    <header class="bg-gray-800 shadow-md w-full z-10">
      <div class="container mx-auto px-4 py-3 flex justify-between items-center">
        <div class="flex items-center">
          <!-- Mobile sidebar toggle -->
          <button 
            @click="sidebarOpen = !sidebarOpen" 
            class="mr-3 text-gray-400 hover:text-white md:hidden"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>
          
          <!-- Logo -->
          <div class="flex items-center">
            <div class="bg-indigo-600 w-10 h-10 rounded-md flex items-center justify-center mr-3">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </div>
            <h1 class="text-xl font-semibold">Parts Identifier</h1>
          </div>
        </div>
        
        <!-- Header Right Content - New Search button -->
        <div>
          <button 
            @click="resetForm" 
            v-if="partsData && partsData.length > 0"
            class="bg-indigo-600 hover:bg-indigo-700 text-white px-4 py-2 rounded-md text-sm transition duration-200"
          >
            New Search
          </button>
        </div>
      </div>
    </header>

    <div class="flex flex-1">
      <!-- Sidebar Navigation -->
      <aside 
        :class="['bg-gray-800 text-gray-300 w-64 min-h-screen md:block transition-all duration-300', 
                 sidebarOpen ? 'block fixed left-0 top-0 h-full z-50 shadow-lg' : 'hidden']"
      >
        <!-- Mobile close button -->
        <div class="md:hidden p-4 flex justify-end" v-if="sidebarOpen">
          <button @click="sidebarOpen = false" class="text-gray-500 hover:text-white">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        
        <nav class="p-5">
          <h2 class="text-xs uppercase tracking-wider text-gray-500 font-semibold mb-3">
            Navigation
          </h2>
          
          <ul class="space-y-2">
            <li>
              <a href="#" class="flex items-center px-2 py-2 rounded-md bg-gray-700 text-white">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-3" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z" />
                </svg>
                Dashboard
              </a>
            </li>
            <li>
              <a href="#" class="flex items-center px-2 py-2 rounded-md hover:bg-gray-700 text-gray-300 hover:text-white transition duration-200">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-3" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M4 3a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V5a2 2 0 00-2-2H4zm12 12H4l4-8 3 6 2-4 3 6z" clip-rule="evenodd" />
                </svg>
                Gallery
              </a>
            </li>
            <li>
              <a href="#" class="flex items-center px-2 py-2 rounded-md hover:bg-gray-700 text-gray-300 hover:text-white transition duration-200">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-3" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd" />
                </svg>
                About
              </a>
            </li>
            <li>
              <a href="#" class="flex items-center px-2 py-2 rounded-md hover:bg-gray-700 text-gray-300 hover:text-white transition duration-200">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-3" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M18 5v8a2 2 0 01-2 2h-5l-5 4v-4H4a2 2 0 01-2-2V5a2 2 0 012-2h12a2 2 0 012 2zM7 8H5v2h2V8zm2 0h2v2H9V8zm6 0h-2v2h2V8z" clip-rule="evenodd" />
                </svg>
                Contact
              </a>
            </li>
            <li>
              <a href="#" class="flex items-center px-2 py-2 rounded-md hover:bg-gray-700 text-gray-300 hover:text-white transition duration-200">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-3" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M11.49 3.17c-.38-1.56-2.6-1.56-2.98 0a1.532 1.532 0 01-2.286.948c-1.372-.836-2.942.734-2.106 2.106.54.886.061 2.042-.947 2.287-1.561.379-1.561 2.6 0 2.978a1.532 1.532 0 01.947 2.287c-.836 1.372.734 2.942 2.106 2.106a1.532 1.532 0 012.287.947c.379 1.561 2.6 1.561 2.978 0a1.533 1.533 0 012.287-.947c1.372.836 2.942-.734 2.106-2.106a1.533 1.533 0 01.947-2.287c1.561-.379 1.561-2.6 0-2.978a1.532 1.532 0 01-.947-2.287c.836-1.372-.734-2.942-2.106-2.106a1.532 1.532 0 01-2.287-.947zM10 13a3 3 0 100-6 3 3 0 000 6z" clip-rule="evenodd" />
                </svg>
                Settings
              </a>
            </li>
          </ul>
        </nav>
      </aside>

      <!-- Main Content Area -->
      <main class="flex-1 pt-12 pb-8 px-4 md:px-8">
        <!-- Parts Grid - Show when data is available -->
        <div v-if="partsData && partsData.length > 0" class="bg-gray-800 rounded-lg p-6 shadow-md mb-8">
          <h3 class="text-xl font-semibold mb-4">Parts Inventory</h3>
          
          <!-- Mobile view: Cards -->
          <div class="md:hidden space-y-4">
            <div 
              v-for="part in partsData" 
              :key="part.part_id"
              class="bg-gray-700 rounded-lg p-4 hover:bg-gray-600 transition duration-200"
            >
              <div class="flex justify-between items-start mb-2">
                <h4 class="font-medium text-lg">{{ part.part_name }}</h4>
                <span class="bg-indigo-600 text-white text-xs px-2 py-1 rounded">{{ part.category }}</span>
              </div>
              <p class="text-gray-300 text-sm mb-1">ID: {{ part.part_id }}</p>
              <p class="text-gray-300 text-sm mb-1">Make: {{ part.car_make }}</p>
              <p class="text-gray-300 text-sm mb-3">{{ part.car_model_year_part.split('#').join(' | ') }}</p>
              <div class="flex justify-between items-center">
                <p class="text-green-400 font-bold">${{ part.price }}</p>
                <p class="text-gray-400 text-sm">{{ part.provider }}</p>
              </div>
              <div class="mt-2 text-sm text-gray-400">
                <p>Location: {{ part.location }}</p>
              </div>
            </div>
          </div>
          
          <!-- Desktop view: Table -->
          <div class="hidden md:block overflow-x-auto">
            <table class="min-w-full divide-y divide-gray-700">
              <thead class="bg-gray-700">
                <tr>
                  <th class="px-4 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">Part Name</th>
                  <th class="px-4 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">ID</th>
                  <th class="px-4 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">Make</th>
                  <th class="px-4 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">Model/Year</th>
                  <th class="px-4 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">Category</th>
                  <th class="px-4 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">Price</th>
                  <th class="px-4 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">Provider</th>
                  <th class="px-4 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">Location</th>
                </tr>
              </thead>
              <tbody class="bg-gray-800 divide-y divide-gray-700">
                <tr 
                  v-for="part in partsData" 
                  :key="part.part_id"
                  class="hover:bg-gray-700 transition duration-150"
                >
                  <td class="px-4 py-3 whitespace-nowrap text-sm font-medium text-white">{{ part.part_name }}</td>
                  <td class="px-4 py-3 whitespace-nowrap text-sm text-gray-300">{{ part.part_id }}</td>
                  <td class="px-4 py-3 whitespace-nowrap text-sm text-gray-300">{{ part.car_make }}</td>
                  <td class="px-4 py-3 whitespace-nowrap text-sm text-gray-300">
                    {{ formatModelYearPart(part.car_model_year_part) }}
                  </td>
                  <td class="px-4 py-3 whitespace-nowrap">
                    <span class="px-2 py-1 text-xs font-medium rounded-full bg-indigo-600 text-white">
                      {{ part.category }}
                    </span>
                  </td>
                  <td class="px-4 py-3 whitespace-nowrap text-sm font-medium text-green-400">${{ part.price }}</td>
                  <td class="px-4 py-3 whitespace-nowrap text-sm text-gray-300">{{ part.provider }}</td>
                  <td class="px-4 py-3 whitespace-nowrap text-sm text-gray-300">{{ part.location }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Chat interface - only show when parts data is available -->
        <div v-if="partsData && partsData.length > 0" class="bg-gray-800 rounded-lg p-6 shadow-md mb-8">
          <h3 class="text-xl font-semibold mb-4">Ask about these parts</h3>
          
          <!-- Chat messages -->
          <div class="bg-gray-700 rounded-lg p-4 mb-4 h-64 overflow-y-auto">
            <div v-if="chatMessages.length === 0" class="text-gray-400 text-center py-10">
              Ask a question about the parts in the inventory
            </div>
            
            <div v-for="(message, index) in chatMessages" :key="index" class="mb-4">
              <!-- User message -->
              <div v-if="message.sender === 'user'" class="flex justify-end">
                <div class="bg-indigo-600 text-white p-3 rounded-lg max-w-xs lg:max-w-md">
                  {{ message.text }}
                </div>
              </div>
              
              <!-- System message -->
              <div v-else class="flex justify-start">
                <div class="bg-gray-600 text-white p-3 rounded-lg max-w-xs lg:max-w-md">
                  {{ message.text }}
                </div>
              </div>
            </div>
            
            <!-- Show typing indicator when loading -->
            <div v-if="chatLoading" class="flex justify-start">
              <div class="bg-gray-600 text-white p-3 rounded-lg">
                <span class="inline-flex items-center">
                  <span class="animate-bounce h-2 w-2 bg-gray-300 rounded-full mr-1"></span>
                  <span class="animate-bounce h-2 w-2 bg-gray-300 rounded-full delay-75 mr-1"></span>
                  <span class="animate-bounce h-2 w-2 bg-gray-300 rounded-full delay-150"></span>
                </span>
              </div>
            </div>
          </div>
          
          <!-- Chat input -->
          <div class="flex space-x-2">
            <input 
              v-model="chatInput" 
              type="text" 
              placeholder="Type your question here..." 
              class="flex-1 bg-gray-700 border border-gray-600 rounded-md py-2 px-3 text-gray-100 focus:outline-none focus:ring-2 focus:ring-indigo-500"
              @keyup.enter="sendChatMessage"
            />
            <button 
              @click="sendChatMessage" 
              class="bg-indigo-600 hover:bg-indigo-700 text-white py-2 px-4 rounded-md transition duration-200 disabled:opacity-50"
              :disabled="!chatInput.trim() || chatLoading"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-8.707l-3-3a1 1 0 00-1.414 1.414L10.586 9H7a1 1 0 100 2h3.586l-1.293 1.293a1 1 0 101.414 1.414l3-3a1 1 0 000-1.414z" clip-rule="evenodd" />
              </svg>
            </button>
          </div>
        </div>
        
        <!-- Upload Section - Only show if no parts data or if explicitly showing upload form -->
        <div v-if="!partsData || partsData.length === 0" class="space-y-8">
          <h2 class="text-2xl font-bold mb-6">Upload Part</h2>
          
          <div class="bg-gray-800 rounded-lg p-6 shadow-md mb-8">
            <div class="mb-4">
              <h3 class="text-xl font-semibold mb-2">Upload a new image</h3>
              <p class="text-gray-400">Supported formats: JPG, PNG, GIF (max 5MB)</p>
            </div>
            
            <!-- Image Upload Area -->
            <div 
              class="border-2 border-dashed border-gray-600 rounded-lg p-8 text-center hover:border-indigo-500 transition duration-200 cursor-pointer"
              @click="triggerFileInput"
              @dragover.prevent="isDragging = true"
              @dragleave.prevent="isDragging = false"
              @drop.prevent="handleFileDrop"
              :class="{ 'border-indigo-500 bg-gray-700 bg-opacity-20': isDragging || imagePreview }"
            >
              <div v-if="!imagePreview">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 mx-auto text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                </svg>
                <p class="mt-3 text-gray-400">Drag and drop your image here, or click to select</p>
              </div>
              
              <div v-else class="relative">
                <img :src="imagePreview" class="max-h-64 mx-auto rounded" alt="Image preview" />
                <button 
                  class="absolute top-2 right-2 bg-gray-900 bg-opacity-70 rounded-full p-1 hover:bg-red-600 transition duration-200"
                  @click.stop="clearImage"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
                  </svg>
                </button>
              </div>
              
              <input 
                type="file" 
                ref="fileInput" 
                class="hidden" 
                accept="image/*" 
                @change="handleFileChange"
              />
            </div>
            
            <!-- Vehicle Information Form -->
            <div class="mt-6 mb-6 bg-gray-700 p-5 rounded-lg">
              <h3 class="text-lg font-medium mb-4">Vehicle Information</h3>
              
              <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <!-- Brand Dropdown -->
                <div>
                  <label for="brand" class="block text-sm font-medium text-gray-300 mb-1">Brand</label>
                  <select 
                    id="brand" 
                    v-model="vehicleInfo.brand" 
                    class="w-full bg-gray-800 border border-gray-600 rounded-md py-2 px-3 text-gray-100 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                  >
                    <option value="" disabled>Select Brand</option>
                    <option v-for="brand in brandOptions" :key="brand" :value="brand">{{ brand }}</option>
                  </select>
                </div>
                
                <!-- Model Dropdown -->
                <div>
                  <label for="model" class="block text-sm font-medium text-gray-300 mb-1">Model</label>
                  <select 
                    id="model" 
                    v-model="vehicleInfo.model" 
                    class="w-full bg-gray-800 border border-gray-600 rounded-md py-2 px-3 text-gray-100 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                  >
                    <option value="" disabled>Select Model</option>
                    <option v-for="model in modelOptions" :key="model" :value="model">{{ model }}</option>
                  </select>
                </div>
                
                <!-- Year Dropdown -->
                <div>
                  <label for="year" class="block text-sm font-medium text-gray-300 mb-1">Year</label>
                  <select 
                    id="year" 
                    v-model="vehicleInfo.year" 
                    class="w-full bg-gray-800 border border-gray-600 rounded-md py-2 px-3 text-gray-100 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                  >
                    <option value="" disabled>Select Year</option>
                    <option v-for="year in yearOptions" :key="year" :value="year">{{ year }}</option>
                  </select>
                </div>
              </div>
            </div>

            <div class="mt-4 flex flex-col sm:flex-row justify-between sm:items-center">
              <div v-if="uploadStatus" class="mb-3 sm:mb-0">
                <p v-if="uploadStatus === 'uploading'" class="text-indigo-400">
                  <svg class="animate-spin h-5 w-5 mr-2 inline" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Uploading...
                </p>
                <p v-else-if="uploadStatus === 'success'" class="text-green-500">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline mr-1" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                  </svg>
                  Upload successful! <a :href="uploadedImageUrl" target="_blank" class="text-indigo-400 hover:underline">View image</a>
                </p>
                <p v-else-if="uploadStatus === 'error'" class="text-red-500">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 inline mr-1" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                  </svg>
                  {{ errorMessage }}
                </p>
              </div>
              <button 
                @click="uploadImage"
                class="bg-indigo-600 hover:bg-indigo-700 text-white py-2 px-6 rounded-md transition duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
                :disabled="!imagePreview || uploadStatus === 'uploading'"
              >
                Upload Image
              </button>
            </div>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      sidebarOpen: false,
      isDragging: false,
      imagePreview: null,
      uploadStatus: null, // 'uploading', 'success', 'error'
      errorMessage: '',
      uploadedImageUrl: '',
      // Replace with your actual Lambda function URL from CloudFormation output
      lambdaFunctionUrl: 'https://ypdhwwcf35ujq3hk4o6z255wo40lnlpl.lambda-url.us-east-1.on.aws/',
      selectedFile: null,
      selectedFileType: '',
      partsData: null, // Will store the returned parts data from API
      
      // Vehicle information form data
      vehicleInfo: {
        brand: '',
        model: '',
        year: ''
      },
      
      // Chat functionality
      chatInput: '',
      chatMessages: [],
      chatLoading: false,
      
      // Dropdown options
      brandOptions: ['BMW','Chrysler', 'Ford', 'Toyota'],
      modelOptions: ['Passenger Car', 'Truck', 'Van'],
      yearOptions: ['2022', '2023', '2024', '2025']
    }
  },

  methods: {
    // Reset everything and start over
    resetForm() {
      this.imagePreview = null;
  this.selectedFile = null;
  this.selectedFileType = '';
  this.uploadStatus = null;
  this.partsData = null;
  this.chatMessages = [];
  this.chatInput = '';
  this.vehicleInfo = {
    brand: '',
    model: '',
    year: ''
  };
  
  // Add this check to prevent the error
  if (this.$refs.fileInput) {
    this.$refs.fileInput.value = '';
  }
},
    
    // File upload methods
    triggerFileInput() {
      this.$refs.fileInput.click();
    },
    handleFileChange(event) {
      const file = event.target.files[0];
      if (file) {
        this.validateAndProcessFile(file);
      }
    },
    handleFileDrop(event) {
      this.isDragging = false;
      const file = event.dataTransfer.files[0];
      if (file && file.type.startsWith('image/')) {
        this.validateAndProcessFile(file);
      }
    },
    validateAndProcessFile(file) {
      // Validate file size (5MB limit)
      const maxSize = 5 * 1024 * 1024; // 5MB in bytes
      if (file.size > maxSize) {
        this.uploadStatus = 'error';
        this.errorMessage = 'Image size exceeds 5MB limit. Please choose a smaller file.';
        return;
      }
      
      this.selectedFile = file;
      this.selectedFileType = file.type;
      this.createImagePreview(file);
    },
    createImagePreview(file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        this.imagePreview = e.target.result;
      };
      reader.onerror = () => {
        this.uploadStatus = 'error';
        this.errorMessage = 'Failed to read the image file. Please try again.';
      };
      reader.readAsDataURL(file);
    },
    clearImage(event) {
      event.preventDefault();
      this.imagePreview = null;
      this.selectedFile = null;
      this.selectedFileType = '';
      this.uploadStatus = null;
      this.partsData = null; // Clear parts data when clearing image
      this.$refs.fileInput.value = '';
    },
    async uploadImage() {
      if (!this.imagePreview) return;
      
      try {
        this.uploadStatus = 'uploading';
        this.partsData = null; // Reset parts data on new upload
        console.log('Starting upload...');
        
        // Generate a unique filename with extension based on content type
        const getExtension = (mimeType) => {
          const extensions = {
            'image/jpeg': 'jpg',
            'image/png': 'png',
            'image/gif': 'gif',
            'image/svg+xml': 'svg',
            'image/webp': 'webp'
          };
          return extensions[mimeType] || 'jpg';
        };
        
        const filename = `image-${Date.now()}.${getExtension(this.selectedFileType)}`;
        console.log(`Generated filename: ${filename}`);
        
        // Prepare payload for Lambda function with vehicle info
        const payload = {
          image: this.imagePreview, // This includes the base64 data
          filename: filename,
          contentType: this.selectedFileType,
          vehicleInfo: {
            brand: this.vehicleInfo.brand,
            model: this.vehicleInfo.model,
            year: this.vehicleInfo.year
          }
        };
        
        console.log('Sending to Lambda:', {
          url: this.lambdaFunctionUrl,
          contentType: this.selectedFileType,
          imageSize: this.imagePreview.length,
          vehicleInfo: this.vehicleInfo
        });
        
        // Send to Lambda function
        const response = await fetch(this.lambdaFunctionUrl, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(payload)
        });
        
        console.log('Response status:', response.status);
        
        // Try to parse the response
        let result;
        try {
          result = await response.json();
          console.log('Response data:', result);
        } catch (jsonError) {
          console.error('Failed to parse response as JSON:', jsonError);
          const textResponse = await response.text();
          console.log('Raw response:', textResponse);
          throw new Error('Invalid response from server');
        }
        
        if (!response.ok) {
          throw new Error(result.error || result.details || 'Upload failed');
        }
        
        this.uploadStatus = 'success';
        this.uploadedImageUrl = result.imageUrl;
        
        // Store the parts data from the response
        if (result.data && Array.isArray(result.data)) {
          this.partsData = result.data;
          console.log('Parts data received:', this.partsData);
        } else {
          console.warn('No parts data found in response');
        }
        
        console.log('Upload completed successfully:', this.uploadedImageUrl);
        
      } catch (error) {
        console.error('Upload error:', error);
        this.uploadStatus = 'error';
        this.errorMessage = error.message || 'Failed to upload image. Please try again.';
      }
    },
    // Format the model year part string
    formatModelYearPart(modelYearPart) {
      if (!modelYearPart) return '';
      
      // Split by # and format nicely
      const parts = modelYearPart.split('#');
      return parts.join(' | ');
    },
    
    // Chat functionality
    sendChatMessage() {
      if (!this.chatInput.trim() || this.chatLoading) return;
      
      // Add user message to chat
      this.chatMessages.push({
        sender: 'user',
        text: this.chatInput.trim()
      });
      
      // Store the message and clear input
      const message = this.chatInput.trim();
      this.chatInput = '';
      
      // Set loading state
      this.chatLoading = true;
      
      // Simulate API call delay
      setTimeout(() => {
        this.handleChatResponse(message);
      }, 1000);
    },
    
    // Handle chat response (will be replaced with actual API integration)
    handleChatResponse(message) {
      // This is a placeholder - replace with actual API call to your chat backend
      let response = '';
      
      // Simple response simulation based on keywords
      const messageLower = message.toLowerCase();
      
      if (messageLower.includes('price') || messageLower.includes('cost')) {
        response = 'The prices for these parts range from $' + 
          Math.min(...this.partsData.map(p => p.price)) + 
          ' to $' + Math.max(...this.partsData.map(p => p.price)) + 
          '. Is there a specific part you\'re interested in?';
      } else if (messageLower.includes('location') || messageLower.includes('where')) {
        const locations = [...new Set(this.partsData.map(p => p.location))];
        response = 'These parts are available at: ' + locations.join(', ');
      } else if (messageLower.includes('brand') || messageLower.includes('make')) {
        const makes = [...new Set(this.partsData.map(p => p.car_make))];
        response = 'These parts are compatible with: ' + makes.join(', ');
      } else {
        response = 'I can provide information about the parts in the inventory. You can ask about prices, locations, compatibility, or specific part details.';
      }
      
      // Add response to chat
      this.chatMessages.push({
        sender: 'system',
        text: response
      });
      
      // End loading state
      this.chatLoading = false;
   
      // Scroll to bottom of chat
      this.$nextTick(() => {
        const chatContainer = document.querySelector('.overflow-y-auto');
        if (chatContainer) {
          chatContainer.scrollTop = chatContainer.scrollHeight;
        }
      });
    }
  }
}
</script>