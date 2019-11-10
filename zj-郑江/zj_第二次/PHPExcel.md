# PHPExcel文件导出，样式控制

看云文档：<https://www.kancloud.cn/shuiyueju/phpexcel/345876> 

- 往指定的单元格内填充值

  ```php
   $objPHPExcel->setActiveSheetIndex(0)->setCellValue('A1', "标题一");
  ```

  

- A1表示第一列，第1行所在单元格的位置。

- 合并单元格

  ```php+HTML
   $objPHPExcel->getActiveSheet()->mergeCells("A1:L1");
  ```

- 据中显示

  ```php
  //所有单元格据中
  $objPHPExcel->getDefaultStyle()->getAlignment()->setHorizontal(PHPExcel_Style_Alignment::HORIZONTAL_CENTER);
  $objPHPExcel->getDefaultStyle()->getAlignment()->setVertical(PHPExcel_Style_Alignment::VERTICAL_CENTER);
  
  //单个单元格据中
  $objPHPExcel->getActiveSheet()->getStyle('A1')->getAlignment()->setHorizontal(PHPExcel_Style_Alignment::HORIZONTAL_CENTER);
  $objPHPExcel->getActiveSheet()->getStyle('A1')->>getAlignment()->setVertical(PHPExcel_Style_Alignment::VERTICAL_CENTER);
  ```

- 设置单元格宽高

  ```php
  $objPHPExcel->getActiveSheet()->getDefaultRowDimension()->setRowHeight(20);#设置单元格行高
  $objPHPExcel->getActiveSheet()->getColumnDimension('A')->setWidth(40);#设置单元格宽度
  $objPHPExcel->getActiveSheet()->getColumnDimension('B')->setWidth(10);
  $objPHPExcel->getActiveSheet()->getColumnDimension('C')->setWidth(20);
  $objPHPExcel->getActiveSheet()->getColumnDimension('D')->setWidth(15);
  
  //设置默认行高
  $objPHPExcel->getActiveSheet()->getDefaultRowDimension()->setRowHeight(15);
  //设置某一行行高
  $objPHPExcel->getActiveSheet()->getRowDimension('9')->setRowHeight(20);
  ```

- 字体加粗

  ```php
  $objPHPExcel->getActiveSheet()->getStyle('A1')->getFont()->setBold(true);
  ```

- 设置字体大小

  ```php
  $objPHPExcel->getActiveSheet()->getStyle("F1:G1")->getFont()->setSize(16);
  ```

- 设置字体

  ```php
  $phpexcel->getActiveSheet()->getStyle('B1')->getFont()->setName('Candara');
  ```

- 设置边框

  ```php
  //设置边框
     $objPHPExcel->getActiveSheet()->getStyle('A1:H8')->getBorders()->getAllBorders()->setBorderStyle(\PHPExcel_Style_Border::BORDER_THIN);
  ```

- 综合样式调整

  ```php
  $style_Array=array(
          'font'    => array (
             'bold'      => true
            ),
           'alignment' => array (
                    'horizontal' => PHPExcel_Style_Alignment::HORIZONTAL_RIGHT ,
             ),
            'borders' => array (
                 'top'     => array (
                         'style' => PHPExcel_Style_Border::BORDER_THIN
                     )
              ),
           'fill' => array (
                  'type'       => PHPExcel_Style_Fill::FILL_GRADIENT_LINEAR ,//填充样式
                   'rotation'   => 90,//填充颜色的方向
                     'startcolor' => array (
                       'argb' => 'FFA0A0A0' //起始颜色
                       ),
                      'endcolor'   => array (
                           'argb' => 'FFFFFFFF'  //结束颜色
                     )
              )
     );
  $objPHPExcel->getActiveSheet()->getStyle( 'A3:E3')->applyFromArray(
  $style_Array            
  );
  ```

  