/**
 * Created with IntelliJ IDEA.
 * User: josephblau
 * Date: 2/2/13
 * Time: 11:31 PM
 * To change this template use File | Settings | File Templates.
 */

$(document).ready(function() {
  $('#short-form').ajaxForm({
    dataType:  'json',
    success: function(data) {
     $('#myModalBody').html(window.location + data.short_code);
     $('#myModal').modal();
     $('#short-form').resetForm();
    }
  });
});