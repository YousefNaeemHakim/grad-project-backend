const mongoose = require("mongoose");

const BookSchema = new mongoose.Schema(
  {
    title: { 
      type: String, required: true, unique: true 
    },
    
    author: { 
      type: string, required: true 
    },
    
    slug: String,
    
    description: {
      type: String,
      required: [true, 'Please add a description'],
      maxlength: [500, 'Description can not be more than 500 characters']
    },
    
    website: {
      type: String,
      match: [
        /https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)/,
        'Please use a valid URL with HTTP or HTTPS'
      ]
    },
    
    price: { 
      type: Number, required: true 
    },
    
    cover: { 
      type: String, required: true 
    },
    
    categories: { 
      type: Array 
    },

    averageRating: {
      type: Number,
      min: [1, 'Rating must be at least 1'],
      max: [10, 'Rating must can not be more than 10']
    },
  },
  { timestamps: true }
);

module.exports = mongoose.model("Book", BookSchema);
