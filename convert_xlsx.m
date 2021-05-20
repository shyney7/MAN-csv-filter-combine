[~,~,a]=xlsread('filtered_timestamp_combined_csv.csv');
b=regexp(a,',','split');
c=reshape([b{:}],numel(b{1}),[])';
writecell(c,'filtered.xlsx')