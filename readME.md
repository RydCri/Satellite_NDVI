### Normalized Difference Vegetation Index (NDVI) 

This project was the result of stumbling upon the Onera Satellite Change Detection dataset hosted on IEEE - Dataport.

<br>

The Onera dataset contains multispectrum satellite images to train a change recognition model. 
<br>
No model was trained for this project, just simple plots visualizing change recognition with one process.<br>
<br>
The Normalized Difference Vegetation Index is a widely used index in agriculture to assess vegetation health and biomass. <br>
<ul>
The formula:
<li>NIR: Near-infrared reflectance, which healthy vegetation strongly reflects.</li>
<li>Red: Red reflectance, which healthy vegetation absorbs strongly.</li>
<li>Calculation: The formula subtracts the red reflectance from the near-infrared reflectance and then divides the result by the sum of the two reflectances.</li>
<h3>NDVI = (NIR - Red) / (NIR + Red)</h3>
</ul>

<br>
<h4>Using the Onera NIR and red band spectrum images, functions were defined to produce plots showing the NDVI of 24 locations on different dates.</h4>
<div>
<img style='height:200px;width:200px;' src='./output/ndvi_change_plot_paris_rect_date1_vs_date2.png' alt='paris'>
<img style='height:200px;width:200px;' src='./output/ndvi_change_plot_mumbai_rect_date1_vs_date2.png' alt='mumbai'>
<img style='height:200px;width:200px;' src='./output/ndvi_change_plot_valencia_rect_date1_vs_date2.png' alt='valencia'>
<img style='height:200px;width:200px;' src='./output/ndvi_change_plot_aguasclaras_rect_date1_vs_date2.png' alt='aguasclaras'>
</div>
<div>
<img style='height:200px;width:200px;' src='./output/ndvi_change_plot_milano_rect_date1_vs_date2.png' alt='milano'>
<img style='height:200px;width:200px;' src='./output/ndvi_change_plot_abudhabi_rect_date1_vs_date2.png' alt='abudhabi'>
<img style='height:200px;width:200px;' src='./output/ndvi_change_plot_nantes_rect_date1_vs_date2.png' alt='nantes'>
<img style='height:200px;width:200px;' src='./output/ndvi_change_plot_montpellier_rect_date1_vs_date2.png' alt='montpellier'>
</div>
<div>
<img style='height:200px;width:200px;' src='./output/ndvi_change_plot_rennes_rect_date1_vs_date2.png' alt='rennes'>
<img style='height:200px;width:200px;' src='./output/ndvi_change_plot_chongqing_rect_date1_vs_date2.png' alt='chongqing'>
<img style='height:200px;width:200px;' src='./output/ndvi_change_plot_rio_rect_date1_vs_date2.png' alt='rio'>
<img style='height:200px;width:200px;' src='./output/ndvi_change_plot_bercy_rect_date1_vs_date2.png' alt='bercy'>
</div>
<div>
<img style='height:200px;width:200px;' src='./output/ndvi_change_plot_bordeaux_rect_date1_vs_date2.png' alt='bordeaux'>
<img style='height:200px;width:200px;' src='./output/ndvi_change_plot_hongkong_rect_date1_vs_date2.png' alt='hongkong'>
<img style='height:200px;width:200px;' src='./output/ndvi_change_plot_pisa_rect_date1_vs_date2.png' alt='pisa'>
<img style='height:200px;width:200px;' src='./output/ndvi_change_plot_norcia_rect_date1_vs_date2.png' alt='norcia'>
</div>
<div>
<img style='height:200px;width:200px;' src='./output/ndvi_change_plot_saclay_e_rect_date1_vs_date2.png' alt='saclay_e'>
<img style='height:200px;width:200px;' src='./output/ndvi_change_plot_beirut_rect_date1_vs_date2.png' alt='beirut'>
<img style='height:200px;width:200px;' src='./output/ndvi_change_plot_dubai_rect_date1_vs_date2.png' alt='dubai'>
<img style='height:200px;width:200px;' src='./output/ndvi_change_plot_saclay_w_rect_date1_vs_date2.png' alt='saclay_w'>
</div>
<div>
<img style='height:200px;width:200px;' src='./output/ndvi_change_plot_beihai_rect_date1_vs_date2.png' alt='beihai'>
<img style='height:200px;width:200px;' src='./output/ndvi_change_plot_brasilia_rect_date1_vs_date2.png' alt='brasilia'>
<img style='height:200px;width:200px;' src='./output/ndvi_change_plot_lasvegas_rect_date1_vs_date2.png' alt='lasvegas'>
<img style='height:200px;width:200px;' src='./output/ndvi_change_plot_cupertino_rect_date1_vs_date2.png' alt='cupertino'>
</div>
<a href='/Onera Satellite Change Detection dataset - Images/Onera - README.txt'>[Attribution: Onera Satellite Change Detection dataset]</a>
