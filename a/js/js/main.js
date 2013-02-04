/**
 * Created with IntelliJ IDEA.
 * User: josephblau
 * Date: 2/2/13
 * Time: 11:31 PM
 * To change this template use File | Settings | File Templates.
 */

$(document).ready(function() {
  $('#short-form').ajaxForm({
    beforeSubmit: function(arr, $form, options){
      // console.log(arr);
//      $("#submit-button").button('loading');
      return true;
    },
    success: function(responseText) {
//      $('#myModalBody').html(JSON.stringify(responseText, null, '<br>'));
//      $('#myModal').modal();
//      $("#submit-button").button('reset');
    }
  });

});