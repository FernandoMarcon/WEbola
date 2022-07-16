function plotVolcano(graphs) {
  Plotly.plot("volcano-plot", graphs, {});
}

function plotGeneExpression(gene_name,cohort,timepoint) {
  const div_name = "gene-boxplot-plot";
  console.log("genes/boxplot/" + gene_name+"/"+cohort+"/"+timepoint)
  fetch("genes/boxplot/" + gene_name+"/"+cohort+"/"+timepoint)
    .then((response) => response.json())
    .then((data) => {
      Plotly.plot(div_name, data, {});
      document.querySelector('.gene_level_analysis-content-gif-expression').style.display='none';
      document.querySelector('.gene_level_analysis-gene-exprs-plot').style.opacity=1;
    });
}

function plotGeneNetwork(gene_name,cohort,timepoint) {
  const div_name = "gene-corr-plot";
  fetch("/genes/corr/" + gene_name+"/"+cohort+"/"+timepoint)
    .then((response) => response.json())
    .then((data) => {
      console.log(data)
      if(data['error']){
        document.querySelector('.gene_level_analysis-content-gif-ntw').style.display='none';
      }
      else{
      var chart = anychart.graph(data);
      chart.container(div_name);

      var nodes = chart.nodes();

      // set the size of nodes
      nodes.normal().height(10);
      nodes.hovered().height(15);
      nodes.selected().height(15);

      // set the fill of nodes
      // nodes.normal().fill("blue");
      nodes.hovered().fill("grey");
      nodes.selected().fill("black");

      // set the stroke of nodes
      nodes.normal().stroke(null);
      nodes.hovered().stroke("#333333", 3);
      nodes.selected().stroke("#333333", 3);

      // allow scrolling the chart with the mouse wheel
      chart.interactivity().scrollOnMouseWheel(true);
      chart.credits(false);
      chart.fit().draw();
      document.querySelector('.gene_level_analysis-content-gif-ntw').style.display='none';
      document.querySelector('#gene-corr-plot').style.opacity=1;
      }
    });
    
      
}

dict_day={
  "USA":["D1","D2","D3","D7"],
  "Geneva":["D1","D2","D3","D7","D14","D21","D28","D35"]
}