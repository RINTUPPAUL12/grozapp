(function($) {
    $(document).ready(function() {
      var subregionSelect = $('#id_subregion');
      var regionSelect = $('#id_region');
      
      // Function to update the region field based on the selected subregion
      function updateRegion() {
        var subregionId = subregionSelect.val();
        if (subregionId) {
          // Make a GET request to the server to get the available regions
          $.get('/admin/myapp/product/get_regions/', {subregion_id: subregionId}, function(data) {
            // Replace the options in the region select field
            regionSelect.html(data);
          });
        }
        // pip install django-multiselectfield
      }
      
      // Initial update of the region field
      updateRegion();
      
      // Update the region field whenever the subregion field changes
      subregionSelect.change(updateRegion);
    });
  })(django.jQuery);
  