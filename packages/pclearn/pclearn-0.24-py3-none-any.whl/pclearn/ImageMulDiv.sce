clc;
clear;
close();
img1 = imread('C:\Users\Admin\Downloads\tomjerry.jpg');
img2 = imread('C:\Users\Admin\Downloads\newtomjerry.jpg');
// Convert to grayscale if images are RGB
if size(img1, 3) == 3 then
    img1 = rgb2gray(img1);
end
if size(img2, 3) == 3 then
    img2 = rgb2gray(img2);
end
// Convert to binary (thresholding)
img1 = img1 > 128;
img2 = img2 > 128;
// Resize second image if sizes are different
if size(img1, 1) ~= size(img2, 1) | size(img1, 2) ~= size(img2, 2) then
    img2 = imresize(img2, [size(img1, 1), size(img1, 2)]);
end
// Perform Multiplication
multiplied_img = img1 .* img2;
// Perform Division
img2(img2 == 0) = 1;  // Avoid division by zero
divided_img = img1 ./ img2;
// Display images
subplot(1, 4, 1);
imshow(img1);
title("Image 1");
subplot(1, 4, 2);
imshow(img2);
title("Image 2");
subplot(1, 4, 3);
imshow(multiplied_img);
title("Image Multiplication Result");
subplot(1, 4, 4);
imshow(divided_img);
title("Image Division Result");
