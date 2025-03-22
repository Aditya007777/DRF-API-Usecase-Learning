from django.db import models

class Blog(models.Model) :
    blog_title = models.CharField(max_length=50)
    blog_content = models.TextField()
    
    def __str__(self):
        return self.blog_title
    

class Comment(models.Model) :
    blog_name = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    
    def __str__(self):
        return self.comment
        
        
        
    
    


    
      
