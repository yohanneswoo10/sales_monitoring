frappe.pages['sales-monitor'].on_page_load = function(wrapper) {
        new MyPage(wrapper);
}

MyPage = Class.extend({
        init: function(wrapper){
		this.page = frappe.ui.make_app_page({
			parent: wrapper,
			title: 'Sales Monitor',
			single_column: true
		});
                // make page
                frappe.require('/assets/sales_monitoring/js/loader.js', ()=>{
                        this.make();
                })
	},
	
	// make page
        make: function(){
                // grab the class
                let me = $(this);
                // push dom elemt to page

                // execute methods
                $(frappe.render_template(`
                                <div style="text-align:center;">
                                <div class="row">SALES ORDER
                                        //<div class="col-md-6"id="chart_div" style="width: 100%; height: 400pxpx;"></div>
                                        <div class="col-md-6"style="width: 100%;" id="desc_table"></div>
                                </div>
                         //<div id="cpu_frequency_div" style="width: 100%; height: 500px;"></div>
                         </div>`, this)).appendTo(this.page.main);
                sales_data();

        }
	// end of class

})

let sales_data = () => {
                setTimeout(()=>{
                        get_sales_order();
                        
                }, 3000)
        }

let get_sales_order = () => {
	frappe.call({
                        method: "sales_monitoring.sales_monitoring.page.sales_monitor.sales_monitor.get_sales_order", //dotted path to server method
                        callback: function(r) {
                                        // code snippet
                                        data = r.message
                                        console.log(r);
                                        document.querySelector('#desc_table').innerHTML = data.desctable;
                        }
        })

}

